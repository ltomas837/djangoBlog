from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
This file define the tables in DB
"""

class Category(models.Model):
    
    name = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique category')
        ]
    
    def __str__(self):
        return self.name


class Article(models.Model):

    title       = models.CharField(max_length=100)
    content     = models.TextField()
    author      = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name="unique article's title")
        ]

    def __str__(self):
        return self.title



class linkArticleCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article  = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'article'], name='unique category/article link')
        ]

    def __str__(self):
        return "'"+self.article.title+"' belongs to category '"+self.category.name+"'"    