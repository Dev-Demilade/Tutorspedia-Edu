import profile
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from .forms import UpdateProfileForm, UpdateUserForm



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def edit_profile(request):
    request.user.userprofile = UserProfile.objects.get_or_create(user=request.userprofile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile is Updated Successfully!')
            return redirect('edit_profile')
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
            
    return render(request, 'uprofile.html', {'user_form': user_form, 'profile_form': profile_form})

def settings(request):
    return render(request, 'settings.html')

def community(request):
    return render(request, 'community.html')
    
# Create your views here.
