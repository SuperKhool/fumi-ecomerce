from django.contrib import admin
from django.urls import path, include
from .views import cart
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',cart,name='cart')

]