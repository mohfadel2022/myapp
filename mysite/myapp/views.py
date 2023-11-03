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
      return render(request, 'myapp/products_list.html', {'items': products})

def product(request, id):
      product = Product.objects.get(id = id)
      return render(request, 'myapp/product.html', {'item': product})


def add_item(request):

      if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image = request.FILES['image']
            item = Product(name=name, price=price, description=description, image=image)
            item.save()

      return render(request, 'myapp/add_item.html')