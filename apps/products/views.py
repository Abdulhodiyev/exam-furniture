from django.shortcuts import render

def products_page_view(request):
    return render(request, 'products/product-cart.html')

def product_checkout_page_view(request):
    return render(request, 'products/product-checkout.html')

def product_detail_page_view(request):
    return render(request, 'products/product-detail.html')

def product_grid_page_view(request):
    return render(request, 'products/product-grid-sidebar-left.html')