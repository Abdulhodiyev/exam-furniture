from django.urls import path

from apps.products.views import products_page_view, product_checkout_page_view, product_detail_page_view, product_grid_page_view

app_name = 'products'

urlpatterns = [
    path('product-grid/', product_grid_page_view, name='grid'),
    path('product-detail/', product_detail_page_view, name='detail'),
    path('product-checkout/', product_checkout_page_view, name='checkout'),
    path('', products_page_view, name='cart')
]