from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

def home(request):
    items = ['iphone', 'samsung', 'xiaomi']
    return HttpResponse(items)

def contact(request):
        return HttpResponse('<h1>  Contacts </h1>')

def products_list(request):
      
      products = Product.objects.all()
      return render(request, 'myapp/products_list.html', {'products': products})

def product(request, id):
      product = Product.objects.get(id = id)
      return render(request, 'myapp/product.html', {'product': product})