from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'user'

urlpatterns = [    
    path('register/', views.register, name='register'),    
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),    
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name= 'profile'),
    path('user_profile/<int:id>/', views.user_profile, name= 'user_profile'),

]