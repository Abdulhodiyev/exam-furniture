from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class ProfileModel(BaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


class CategoryModel(BaseModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TagModel(BaseModel):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class PostModel(BaseModel):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=255)
    description = RichTextUploadingField(blank=True, null=True)


    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    tags = models.ManyToManyField(
        TagModel,
        related_name='posts'
    )
