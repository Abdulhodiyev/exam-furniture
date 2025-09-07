from django.shortcuts import render


from apps.blogs.models import PostModel, CategoryModel, TagModel


def blogs_list_view(request):
    posts = PostModel.objects.all()
    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'blogs/blog-list-sidebar-left.html', context)


def blogs_detail_view(request, pk):
    try:
        post = PostModel.objects.get(id=pk)
    except PostModel.DoesNotExist:
        return render(request, 'pages/404.html')

    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()
    related_posts = PostModel.objects.filter(
        category=post.category
    ).exclude(id=post.id)
    context = {
        'post': post,
        'categories': categories,
        'tags': tags,
        'related_posts': related_posts,
    }
    return render(request, 'blogs/blog-detail.html', context)
