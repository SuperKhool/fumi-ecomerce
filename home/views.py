from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def shop(request):
    return render(request,'home/shop.html')

def services(request):
    return render(request,'home/services.html')

def blog(request):
    return render(request,'home/blog.html')

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

