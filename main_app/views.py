from django.shortcuts import render, HttpResponse, redirect
from .models import Project, Skill

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def skills(request): 
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'skills.html', context)

# Projects Page
def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def contact(request): 
    return render(request, 'contact.html')