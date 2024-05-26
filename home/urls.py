from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('shop/',shop,name='shop'),
    path('about/',about,name='about'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),

]