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



def skill_projects(request, skill_id):
  skill = Skill.objects.get(id=skill_id)
  context = {
      'skill': skill,
      # these are all the variables we're passing to our template
  }
  return render(request, 'skill_projects.html', context)
    # The skill_projects function is using the get method to obtain the skill object by its id.
    # django will pass any captured URL parameters as a named argument to the view function!

# Projects Page
def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def contact(request): 
    return render(request, 'contact.html')