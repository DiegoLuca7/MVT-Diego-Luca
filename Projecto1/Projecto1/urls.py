"""Projecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Projecto1.views import hello_world, bye_world , fecha_actual , vista_con_template, familia_template, regalos_template

from appcoder.views import create_products , list_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hello_world),
    path('chau/', bye_world),
    path('hora/', fecha_actual),
    path('vista-con-template/', vista_con_template),
    path('familia-template/', familia_template),
    path('regalos-template/', regalos_template),

    path('create-products/', create_products),
    path('list-products/' , list_products)
]
