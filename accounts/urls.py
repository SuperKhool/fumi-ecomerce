from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sing_in/',sing_in,name='sing_in' ),
    path('sing_up/',sing_up,name='sing_up'),

]