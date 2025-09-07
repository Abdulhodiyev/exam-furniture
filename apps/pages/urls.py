from django.urls import path

from apps.pages.views import home_page_view, contact_page_view, n404_page_view, about_us_page_view, user_wishlist_page_view

app_name = 'pages'

urlpatterns = [
    path('user-wishlist/', user_wishlist_page_view, name='user-wishlist'),
    path('about-us/', about_us_page_view, name='about-us'),
    path('404/', n404_page_view, name='404'),
    path('contact/', contact_page_view, name='contact'),
    path('', home_page_view, name='home')
]
