from django.urls import path

from apps.products.views import products_page_view, product_checkout_page_view, product_cart_page_view, product_detail_view

app_name = 'products'

urlpatterns = [
    path('product-grid/', product_detail_view, name='detail'),
    path('product-detail/', product_cart_page_view, name='cart'),
    path('product-checkout/', product_checkout_page_view, name='checkout'),
    path('', products_page_view, name='product')
]