import json
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CategoryForm,ProjectForm,StudentProfileForm,PictureForm,VideoForm
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required



def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'index.html',context)

def aboutpage(request):
    return render(request,'about.html')


@login_required
def dashboard(request):
    # try:
    profile = StudentProfile.objects.filter(user=request.user).first()
    if profile is not None:
        projects = Project.objects.filter(student=profile)
        form = ProjectForm()
        if request.method == 'POST':
            form = ProjectForm(request.POST,request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.student = profile
                project.likes = 0
                project.save()
                return redirect('main:dashboard')
        context = {
            'profile':profile,
            'projects':projects,
            'form':form
        }
        return render(request,'dashboard.html',context)
    # except Exception as e:
    else:
        # print(e)
        profile = None
        form = StudentProfileForm()
        if request.method == 'POST':
            form = StudentProfileForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('main:dashboard')
        return render(request,'dashboard.html',{'profileform':form})   

def profile_edit(request,id):
    profile = StudentProfile.objects.get(id=id)
    form = StudentProfileForm(instance=profile)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'profile_edit.html',context)

def all_projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'portfolio.html',context)

def project_details(request,id):
    project = Project.objects.get(id=id)
    context = {
        'project':project
    }
    return render(request,'project_details.html',context)

def project_like(request,id):
    project = Project.objects.get(id=int(id))
    project.likes += 1
    project.save()
    return json.dumps({'likes':project.likes})

def project_unlike(request,id):
    project = Project.objects.get(id=int(id))
    project.likes -= 1
    project.save()
    return json.dumps({'likes':project.likes})

def project_delete(request,id):
    project = Project.objects.get(id=int(id))
    project.delete()
    return redirect('main:dashboard')

def project_edit(request,id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('main:dashboard')
    context = {
        'form':form
    }
    return render(request,'project_edit.html',context)

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
