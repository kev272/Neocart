
from django.contrib import admin
from django.urls import path
from NeoApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('starter/',views.starter,name='starter'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('services/',views.service,name='service'),
    path('team/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
#mpesa api
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),




]
