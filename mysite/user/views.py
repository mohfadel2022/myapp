from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import NewUserForm

from .models import Profile

def register(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    form = NewUserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
      if request.method == 'POST':
            user = request.user
            phone_number = request.POST.get('phone_number')
            image = request.FILES['image']
            profile = Profile(user=user, phone_number=phone_number,image=image)
            profile.save()
      
      return render(request, 'user/profile.html')

def user_profile(request, id):
     user = User.objects.get(id=id)
     profile = Profile.objects.get(user=user)
     context = {
          'profile': profile
     }
     return render(request, 'user/user_profile.html', context)
     