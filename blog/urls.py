from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('loadArticles', views.ArticleList.as_view()),
    path('loadCategories', views.CategoryList.as_view()),
    path('articleDetails/', views.article_details),
]
