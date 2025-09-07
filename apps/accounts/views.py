from django.shortcuts import render

def user_account(request):
    return render(request, 'accounts/user-account.html')

def user_login(request):
    return render(request, 'accounts/user-login.html')

def user_register(request):
    return render(request, 'accounts/user-register.html')

def user_reset_password(request):
    return render(request, 'accounts/user-reset-password.html')