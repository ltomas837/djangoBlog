from django.contrib import admin
from .models import Category, Article, linkArticleCategory


class ArticleAdmin(admin.ModelAdmin):

    """
    Auto-assign the user when creating an article in the admin page
    """
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

    """
    The code below manage some fields to be read-only
    """

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ['title'] + [f.name for f in obj._meta.fields if not f.editable]
        return self.readonly_fields

    def get_fields(self, request, obj=None):
        if obj:
            return ['title', 'content', 'author', 'date_posted']
        return ['title', 'content']



class CategoryAdmin(admin.ModelAdmin):

    """
    The code below manage some fields to be read-only
    """
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name']
        return self.readonly_fields



admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(linkArticleCategory)

