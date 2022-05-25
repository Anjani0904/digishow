from django import forms
from .models import Category,Project,StudentProfile,Picture,Video

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('icon','name')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project       
        fields = ('title','category','description','hero_img')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('user','full_name','photo','course')

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('project','image')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('project','video')