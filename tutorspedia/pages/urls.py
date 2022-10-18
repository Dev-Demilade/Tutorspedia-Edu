from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.home,name='home'),
    path('blog', views.blog, name='blog'),
    path('courses', views.courses, name='courses'),
    path('courses/course_detail/<int:course_id>{{course.course_name}}', views.course_detail, name='course_detail'),
    path('courses/search', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('about_us', views.about_us, name='about_us'),
    path('event/', views.event, name='event'),
    path('contact_us', views.contact_us, name='contact_us'),
    path("instructors", views.instructors, name='instructors')

]