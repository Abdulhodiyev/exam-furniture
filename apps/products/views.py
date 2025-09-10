from django.shortcuts import render

from apps.products.models import ProductCategory, ProductCatalog, ProductColor, ProductModel


def products_page_view(request):
    categories = ProductCategory.objects.all()
    manufactures = ProductCatalog.objects.filter(type=ProductCatalog.MANUFACTURE)
    category = ProductCatalog.objects.filter(type=ProductCatalog.CATEGORY)
    colors = ProductColor.objects.all()
    products = ProductModel.objects.all()

    cat_id = request.GET.get('cat')
    color_id = request.GET.get('color')
    category_id = request.GET.get('category')
    manufacture_id = request.GET.get('manufacture')
    q = request.GET.get('q')

    if cat_id:
        products.filter(categories=cat_id)
    if color_id:
        products.filter(categories=color_id)
    if category_id:
        products.filter(categories=category_id)
    if manufacture_id:
        products.filter(categories=manufacture_id)
    if q:
        products.filter(title__icontains=q)

    context = {
        "categories": categories,
        "category": category,
        "manufactures": manufactures,
        "colors": colors,
        "products": products,
    }
    return render(request, 'products/product.html', context)

def product_checkout_page_view(request):
    return render(request, 'products/product-checkout.html')

def product_cart_page_view(request):
    return render(request, 'products/product-cart.html')

def product_detail_view(request):
    return render(request, 'products/product-detail.html')