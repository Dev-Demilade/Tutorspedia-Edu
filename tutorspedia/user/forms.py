from django import forms
from django import forms

from django.contrib.auth.models import User
from django.forms import EmailField
from .models import *


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class':'forms-comtrol'}))
    email = EmailField(required=True,
                       widget=forms.TextInput(attrs={'class':'forms-comtrol'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
        

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class':'forms-comtrol-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'forms-comtrol', 'rows': 5}))
    
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']