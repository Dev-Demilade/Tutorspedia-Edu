from django.urls import reverse
from django.db import models
from PIL import Image


class WorldWideStudent(models.Model):
    number_of_students = models.CharField(max_length=100)
    
class AvailableCourse(models.Model):
    number_of_available_courses = models.CharField(max_length=100)

class ExpertInstructor(models.Model):
    number_of_instructors = models.CharField(max_length=100)

class WebStatistic(models.Model):
    number_of_students_enrolled = models.CharField(max_length=10)
    number_of_uploaded_courses = models.CharField(max_length=10)
    number_of_certified_students = models.CharField(max_length=10)
    number_of_global_instructors = models.CharField(max_length=10)
    
class FeaturedCourse(models.Model):
    course_name = models.CharField(max_length=500)
    course_image = models.ImageField(upload_to='web_images')
    price = models.IntegerField()
    tutor_name = models.CharField(max_length=200)
    tutor_image = models.ImageField(upload_to='web_images')
    reviews = models.CharField(max_length=100)
    likes = models.CharField(max_length=100)
    student_user = models.CharField(max_length=100)
    ratings = models.FloatField(max_length=2)
    
    
            
    
class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='web_images')
    portfolio = models.TextField(max_length=500)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='web_images')
    testimony = models.TextField(max_length=500)
    qualifications = models.TextField(max_length=500)
    
class FeaturedBlog(models.Model):
    author = models.CharField(max_length=200)
    title = models.TextField(max_length=200)
    body = models.TextField(max_length=1569)
    image = models.ImageField(upload_to='web_images')
    date = models.DateField()  
      
class AspectField(models.Model):
    field_name = models.TextField(max_length=100)
    icon = models.ImageField(upload_to='web_images') 
    field_color = models.IntegerField(1)
    
class Partner(models.Model):
    logo = models.ImageField(upload_to='web_images')
    
class Event(models.Model):
    event_title = models.CharField(max_length=500)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Categorie(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering=('category',)



class Course(models.Model):
    ###### Course Info #############
    course_name = models.CharField(max_length=500)
    course_image = models.ImageField(upload_to='web_images')
    price = models.IntegerField()
    course_summary = models.TextField(max_length=450)
    course_duration = models.TextField(max_length=15)
    course_requirement = models.TextField(max_length=450)
    reviews = models.CharField(max_length=100)
    likes = models.CharField(max_length=100)
    student_user = models.CharField(max_length=100)
    ratings = models.FloatField(max_length=2)
    
    ##### Instructor's Information ##########
    tutor_name = models.CharField(max_length=200)
    tutor_image = models.ImageField(upload_to='web_images')
    tutor_portfoilo = models.TextField(max_length=35)
    about_tutor = models.TextField(max_length=350)
    tutor_facebook_profile_link = models.URLField()
    tutor_twitter_profile_link = models.URLField()
    tutor_instagram_profile_link = models.URLField()
    tutor_google_profile_link = models.URLField()
    
    
    def save(self, *args, **kwargs):
        super().save()
        
        img = Image.open(self.tutor_image.path)
        
        if img.height > 25 or img.width > 25:
            new_img = (25, 25)
            img.thumbnail(new_img)
            img.save(self.tutor_image.path)
    
    class Meta:
        ordering = ('course_name',)
    
    def __str__(self):
        return self.course_name
    
    def get_url(self):
        return reverse('course_detail', args=[self.id])
    
    
    
class Blog(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='web_images')
    author = models.CharField(max_length=100)
    aspect = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateField()       
# Create your models here.


# Create your models here.
