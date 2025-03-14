from urllib import request

from django.db import models
from django.shortcuts import render


# Create your models here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def starter(request):
    return render(request,'starter-page.html')

def portfolio(request):
     return render(request, 'portfolio-details.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def service(request):
    return render(request, 'service-details.html')
