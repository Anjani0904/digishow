from email import message
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    icon = models.ImageField(upload_to="icons")
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, unique=True)
    photo=models.ImageField(upload_to='images/', blank=True, null=True)
    course=models.CharField(max_length=75)
    created_on=models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    hero_img=models.ImageField(upload_to='images/', blank=True, null=True)
    likes=models.PositiveIntegerField()
    added_on=models.DateTimeField(auto_now_add=True)
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    email = models.EmailField(max_length=30)

    message=models.TextField(max_length=30)



class Picture(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
        
class Video(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    video=models.FileField()





     

        

