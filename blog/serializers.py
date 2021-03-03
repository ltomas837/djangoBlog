from rest_framework import serializers
from .models import Article, Category

"""
    Define the serialize to serialize data from DB queries on articles
    to sent to the controllers
"""
class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'date_posted']

"""
    Define the serialize to serialize data from DB queries on categories
    to sent to the controllers
"""
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
