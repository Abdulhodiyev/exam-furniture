from django.contrib import admin

from apps.blogs.models import CategoryModel, TagModel, UserModel, PostModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['created_at']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title', 'post']
    list_filter = ['created_at']
