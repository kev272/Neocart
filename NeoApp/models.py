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
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"
class Pricing(models.Model):
    def __str__(self):
        return self
