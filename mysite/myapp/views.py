from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import json
import stripe


from .models import Product , OrderDetail

def contact(request):
        return HttpResponse('<h1>  Contacts </h1>')

def home(request):
      items = Product.objects.all()

      item_name = request.GET.get('search')
      if item_name == '' or item_name is None:
           page_obj = items 
      else:
            page_obj = items.filter(name__icontains= item_name)

      paginator = Paginator(page_obj, 3)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)

      context = {
            'page_obj':page_obj
      }
      return render(request, 'myapp/home.html', context)

# def product(request, id):
#       product = Product.objects.get(id = id)
#       return render(request, 'myapp/product.html', {'item': product})

class ProductListView(ListView):
      model = Product
      template_name = 'myapp/product_list.html'
      context_object_name = 'items'
      paginate_by =3

class ProductDetailView(DetailView):
      model = Product
      template_name = 'myapp/product.html'
      context_object_name = 'item'
      pk_url_kwarg = 'pk'

      def get_context_data(self, **kwargs):
            context =  super(ProductDetailView, self).get_context_data(**kwargs)
            context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
            return context


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

class ProductDeleteView(DeleteView):
      model = Product
      success_url = reverse_lazy('myapp:home')

@csrf_exempt
def create_checkout_session(request, id):

      product =get_object_or_404(Product, pk=id)
      stripe.api_key = settings.STRIPE_SECRET_KEY
      checkout_session = stripe.checkout.Session.create(
            customer_email = request.user.email,
            payment_method_types= ['card'],
            line_items=[
                  {
                        'price_data':{
                              'currency': 'usd',
                              'product_data': {
                                    'name': product.name,
                              },
                              'unit_amount': int(product.price*100),
                        },
                        'quantity': 1,
                  }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('myapp:success'))+"?session_id={CHECKOUT_SESSION_ID}",
            # success_url="http://localhost:8000/success",

            cancel_url=request.build_absolute_uri(reverse('myapp:failed')),
      )
      order = OrderDetail()
      order.customer = request.user.username
      order.product = product
      order.stripe_payment_intent  = checkout_session.id
      order.amount = int(product.price*100)
      order.save()
      return JsonResponse({'sessionId': checkout_session.id})

class PaymentSuccessView(TemplateView):
      template_name = 'myapp/payment_success.html'

      def get(self, request, *args, **kwargs):
            session_id = request.GET.get('session_id')
            if session_id is None:
                  return HttpResponseNotFound()
            session = stripe.checkout.Session.retrieve(session_id)
            stripe.api_key = settings.STRIPE_SECRET_KEY
            order = get_object_or_404(OrderDetail, stripe_payment_intent = session.id)
            order.has_paid = True
            order.save()
            return render(request, self.template_name)
      
class PaymentFailedView(TemplateView):
      template_name = 'myapp/payment_failed.html'

