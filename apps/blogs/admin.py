from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.blogs.models import CategoryModel, TagModel, UserModel, PostModel

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(TagModel)
class TagModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(UserModel)
class UserModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['created_at']


@admin.register(PostModel)
class PostModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title', 'post']
    list_filter = ['created_at']