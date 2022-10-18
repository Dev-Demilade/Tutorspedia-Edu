from zoneinfo import available_timezones
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    
    courses = FeaturedCourse.objects.all()
    teams = OurTeam.objects.all()   
    testimonials = Testimonial.objects.all()
    featured_blogs = FeaturedBlog.objects.all()
    fields = AspectField.objects.all()
    partners = Partner.objects.all()
    events = Event.objects.all()
    students = WorldWideStudent.objects.all()
    available_courses = AvailableCourse.objects.all()
    webstatistics = WebStatistic.objects.all()
    expertinstructors = ExpertInstructor.objects.all()
    
    
    
     
    return render (request, 'index.html', {'courses': courses, 'teams': teams,
                                             'testimonials': testimonials,
                                             'blogs': featured_blogs, 
                                             'fields': fields, 
                                             'partners': partners, 
                                             'events': events, 
                                             'students': students, 
                                             'available_courses': available_courses,
                                             'webstatistics': webstatistics,
                                             'expertinstructors' : expertinstructors
                                             })

def blog(request):
    
    blogs = Blog.objects.all()
    
    return render(request, 'blog.html', {'blogs': blogs})

def courses(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses-singel.html', {'course': course})# 'type': t.category})
    
def search(request):
    
    results = []
    if request.method == 'GET':
        query = request.GET.get('q')
        
        if query == '':
            query == None
        results = Course.objects.filter(Q(course_name__icontains=query) | Q(tutor_name__icontains=query) | Q(price__icontains=query) )
            
    return render(request, 'search.html', {'query': query, 'results': results,})

def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'events.html')

def instructors(request):
    return render(request, 'teachers.html')

def cart(request):
    return render(request, 'cart.html')

# Create your views here.
