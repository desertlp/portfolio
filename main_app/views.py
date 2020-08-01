from django.shortcuts import render, HttpResponse, redirect



class Project:
  def __init__(self, name):
    self.name = name

projects = [
  Project('Takeuchi Tamagotchi'), 
  Project('PartyWave')
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
