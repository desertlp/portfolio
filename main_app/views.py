from django.shortcuts import render
from django.http import HttpResponse

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
    # return HttpResponse('loop throught the project db')
    return render (request, 'index.html')

def contact(request): 
    # return HttpResponse('this should be a form')
    return render(request, 'contact.html')
