from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'main/home-index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def user_register(request):
    return render(request, 'main/home-user-register.html')

def user_login(request):
    return render(request, 'main/home-userlogin.html')


