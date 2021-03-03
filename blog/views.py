from .models import Article, Category, linkArticleCategory
from .serializers import ArticleSerializer, CategorySerializer 
from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.response import Response
from math import ceil
from django.db.models import Q
from django.urls import reverse



def home(request):
    return render(request, "home.html")

def article_details(request):
    if (request.method == 'GET'):
        article = Article.objects.get(id=request.GET['id'])
        context = { 'title'       : article.title,
                    'content'     : article.content,
                    'author'      : article.author.username,
                    'date_posted' : article.date_posted }
        return render(request, "article_details.html", context)
    return render(request, "article_details.html")  



"""
    This class takes care of the get requests to /loadArticles
"""
class ArticleList(generics.ListCreateAPIView):

    serializer_class = ArticleSerializer
    category         = "Any category"
    search           = ""
    articles         = Article.objects.all()
    queryset         = articles.order_by('-date_posted')
    
    def get(self, request, *args, **kwargs):

        ######## Load articles depending on the category ########

        if (self.category != request.GET['category']): # if a new category has been clicked, in order to avoid querying when the category is the same

            self.category = request.GET['category']

            if (self.category != "Any category"):
         
                self.articles = Article.objects.filter(linkarticlecategory__in=Category.objects.get(name=self.category).linkarticlecategory_set.all()).select_related()
            else:
                self.articles = Article.objects.all()

            self.search = request.GET['search']
            self.queryset = self.articles.filter( Q(title__contains=self.search) | Q(content__contains=self.search) ).order_by('-date_posted')

        elif (self.search != request.GET['search']): # if ONLY the input search is different, etc..
            self.search = request.GET['search']
            self.queryset = self.articles.filter( Q(title__contains=self.search) | Q(content__contains=self.search) ).order_by('-date_posted')


        ###### Piece of code fetched from the doc, don't change it ######

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        #################################################################
                                        
        ###### Load page numbering ######
        '''
        numberOfArticles could be a attribute of the rest controller to avoid calculating
        at each get but in this case there are errors on page numbering when adding 
        articles until restarting the server
        '''
        numberOfArticles = len(serializer.data)

        if ( request.GET['page'] == "last" ):
            page  = ceil(numberOfArticles/3)
        else:     
            page  = int(request.GET['page'])
        
        index = (page-1)*3
        firstPage = max(1, page-2)
        lastPage  = min(ceil(numberOfArticles/3), page+2)
    
        pages = []
        if ( 1 < (page-2) ):
            pages.append("..")
        for i in range (firstPage, lastPage+1):
            pages.append(str(i))
        if ( (page+2) < ceil(numberOfArticles/3) ):
            pages.append("..")
        

        ###### Sending serialized data ######

        response = {'currentPage': str(page),
                    'pages'      : pages,
                    'articles'   : serializer.data[index:(index+3)],
        }
        return Response(response)


    

"""
    This class takes care of the get requests to /loadCategories
"""
class CategoryList(generics.ListCreateAPIView):

    queryset         = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer 


    def list(self, request, *args, **kwargs):

        ###### Piece of code fetched from the doc, don't change it ######

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        #################################################################

        if ( (request.method == 'GET')):
            response = {'categories': serializer.data}
            return Response(response)
        return Response([])


