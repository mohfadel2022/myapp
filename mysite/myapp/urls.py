from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name= 'home'),
    # path('', views.ProductListView.as_view() , name= 'home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name= 'product'),
    path('add_item', views.add_item, name= 'add_item'),
    path('update_item/<int:item_id>/', views.update_item, name= 'update_item'),
    # path('delete_item/<int:item_id>/', views.delete_item, name= 'delete_item'),
    path('delete_item/<int:pk>/', views.ProductDeleteView.as_view(), name= 'delete_item'),
    path('success/', views.PaymentSuccessView.as_view(), name= 'success'),
    path('failed/', views.PaymentFailedView.as_view(), name= 'failed'),
    path('api/checkout-session/<int:id>/', views.create_checkout_session, name= 'api_checkout_session'),


    path('contact/', views.contact, name= 'contact'),

]