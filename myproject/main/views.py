from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CategoryForm,ProjectForm,StudentProfileForm,PictureForm,VideoForm
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request,'index.html')

def aboutpage(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

    
def portfolio(request):
    return render(request,'portfolio.html')

def we_do(request):
    return render(request,'we_do.html')

@login_required
def student_view(request):
    form = StudentProfileForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'dashboard.html', ctx)

@login_required
def project_view(request):
    form = ProjectForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'dashboard.html', ctx)

    
def category_view(request):
    form = CategoryForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Data  has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'dashboard.html', ctx)

def picture_view(request):
    form = PictureForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'dashboard.html', ctx)

def video_view(request):
    form = VideoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been successfully added.')
            return redirect('dashboard')
    ctx = {
        'form': form,
    }
    return render(request, 'dashboard.html', ctx)

def contact_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # print(name, email, message, subject)
        if name and email and message:
            messages.success(request, 'Your message has been sent successfully.')
        elif not name:
            messages.error(request, 'Please enter your name.')
        elif not email:
            messages.error(request, 'Please enter your email.')
        elif not message:
            messages.error(request, 'Please enter your message.')
        return redirect('contact')
    return render(request, 'contact.html')
