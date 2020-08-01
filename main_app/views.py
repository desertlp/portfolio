from django.shortcuts import render
from django.http import HttpResponse

# TEMPORARY PROJECTS DATA 
class Project:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, project_url, company, description, timeframe, deployment_date):
    self.name = name
    self.project_url = project_url
    self.company = company
    self.description = description
    self.timeframe = timeframe
    self.deployment_date = deployment_date

projects = [
  Project('Takeuchi Tamagotchi', 'https://desertlp.github.io/tamagotchi/', 'General Assembly', 'first project', '72 hours', '6-26-2020'),
  Project('PartyWave', 'https://desertlp.github.io/PartyWave/', 'General Assembly', 'first team project', '5 days', '7-15-2020'),
]


# HOME 
def home(request):
    # return HttpResponse('get ready bitch, its portfolio time')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('about me page')
    return render(request, 'about.html')
 
def skills(request): 
    # return HttpResponse('list ya skills out hoe')
    return render(request, 'skills.html')

def projects(request): 
    # projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render (request, 'index.html', context)
    # return render(request, 'cats/index.html', context)

def contact(request): 
    # return HttpResponse('this should be a form')
    return render(request, 'contact.html')
