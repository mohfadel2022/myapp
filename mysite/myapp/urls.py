from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('contact/', views.contact, name= 'contact'),
    path('', views.products_list, name= 'product_list'),
    path('product/<int:id>', views.product, name= 'product'),
    path('add_item', views.add_item, name= 'add_item'),

]