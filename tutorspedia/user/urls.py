from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.edit_profile, name = 'edit_profile'),
    path('settings/', views.settings, name='settings'),
    path('join-community/', views.community, name='community'),
]