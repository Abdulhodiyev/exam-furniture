from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from apps.blogs.models import PostModel, TagModel, CategoryModel, UserModel


@register(PostModel)
class NewTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(TagModel)
class NewTranslationOptions(TranslationOptions):
    fields = ['title',]


@register(CategoryModel)
class NewTranslationOptions(TranslationOptions):
    fields = ['title',]


@register(UserModel)
class NewTranslationOptions(TranslationOptions):
    fields = ['full_name',]