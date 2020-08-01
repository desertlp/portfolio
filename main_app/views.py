from django.shortcuts import render, HttpResponse, redirect

class Project:
  def __init__(self, name, project_url, description, deployment_date):
    self.name = name
    self.project_url = project_url
    self.description = description
    self.deployment_date = deployment_date

projects = [
  Project('Takeuchi Tamagotchi', 'https://desertlp.github.io/tamagotchi/', 'first project, 3 days, solo', 'June 26th, 2020'), 
  Project('PartyWave', 'https://secure-mountain-38318.herokuapp.com/', 'second project, 5 days, team project will adams', 'July 15th, 2020' ),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def skills(request): 
    return render(request, 'skills.html')

# projects page
def index(request):
    return render(request, 'index.html', { 'projects': projects })

def contact(request): 
    return render(request, 'contact.html')