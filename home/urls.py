from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.register,name='register'),
    path('log_in', views.log_in,name='log_in'),
    path('homepage', views.homepage,name='homepage'),
   # path('about', views.about,name='about'),
    path('myuploads', views.myuploads,name='myuploads'),
    path('reports', views.reports,name='reports'),
    path('homepage', views.homepage, name='homepage'),
    path('upload', views.upload_call, name='upload_call')
]