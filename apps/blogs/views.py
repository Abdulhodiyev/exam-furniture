from msilib.schema import ListView


from apps.blogs.models import PostModel, CategoryModel, TagModel
from apps.products.models import ProductModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list-sidebar-left.html'

    def get_get_context_data(self, *args, **kwargs):
        context =super().get_get_context_data(*args, **kwargs)
        posts = PostModel.objects.all()
        categories = CategoryModel.objects.all()
        tags = TagModel.objects.all()

        context["blogs"] = self.get_queryset()
        context["posts"] = posts
        context["categories"] = categories
        context["tags"] = tags

        return context


class BlogDetailView(ListView):
    template_name = 'blogs/blog-detail.html'
    queryset = BlogListView.objects.all()
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        categories = CategoryModel.objects.all()
        tags = TagModel.objects.all()
        related_posts = PostModel.objects.filter(
            tags__in=post.tags.all()
        ).exclude(id=post.id).distinct()

        context["blogs"] = self.get_queryset()
        context["categories"] = categories
        context["tags"] = tags
        context["related_posts"] = related_posts

        return context