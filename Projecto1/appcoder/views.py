from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import camisetas


# Create your views here.

def create_products(request):
    camisetas.objects.create(name = "Camiseta Brasil Suplente" , price = 185000 , stock = True )
    return HttpResponse("Se creó el nuevo producto") 

def list_products(request):
    all_products = camisetas.objects.all
    context = {"products" : all_products,
    }
    return render(request, "list_products.html" , context= context)
