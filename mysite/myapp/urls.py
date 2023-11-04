from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('', views.products_list, name= 'home'),
    path('', views.ProductListView.as_view() , name= 'home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name= 'product'),
    path('add_item', views.add_item, name= 'add_item'),
    path('update_item/<int:item_id>/', views.update_item, name= 'update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name= 'delete_item'),


    path('contact/', views.contact, name= 'contact'),

]