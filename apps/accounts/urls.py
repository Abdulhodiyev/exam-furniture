from django.urls import path

from apps.accounts.views import user_account, user_login, user_register, user_reset_password

app_name = 'accounts'

urlpatterns = [
    path('user-password/', user_reset_password, name='reset-password'),
    path('user-register/', user_register, name='register'),
    path('user-login/', user_login, name='login'),
    path('', user_account, name='account')
]