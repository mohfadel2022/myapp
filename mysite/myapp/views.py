from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .models import Product

def contact(request):
        return HttpResponse('<h1>  Contacts </h1>')

# def product_list(request):
      
#       products = Product.objects.all()
#       return render(request, 'myapp/product_list.html', {'items': products})

# def product(request, id):
#       product = Product.objects.get(id = id)
#       return render(request, 'myapp/product.html', {'item': product})

class ProductListView(ListView):
      model = Product
      template_name = 'myapp/product_list.html'
      context_object_name = 'items'

class ProductDetailView(DetailView):
      model = Product
      template_name = 'myapp/product.html'
      context_object_name = 'item'


@login_required
def add_item(request):

      if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image = request.FILES['image']
            user = request.user
            item = Product(name=name, price=price, description=description, image=image, user=user)
            item.save()

      return render(request, 'myapp/add_item.html')

def update_item(request, item_id):

      item = Product.objects.get(id = item_id)
      if request.method == 'POST':
            item.name = request.POST.get('name')
            item.price = request.POST.get('price')
            item.description = request.POST.get('description')
            item.image = request.FILES.get('image', item.image)
            item.save()
            return redirect('/')
      context = {
            'item': item
      }

      return render(request, 'myapp/update_item.html', context)

def delete_item(request, item_id):

      item = Product.objects.get(id = item_id)
      if request.method == 'POST':
            item.delete()
            return redirect('/')
      context = {
            'item': item
      }

      return render(request, 'myapp/delete_item.html', context)

