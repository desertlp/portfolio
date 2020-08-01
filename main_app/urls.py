from django.urls import path
from . import views

urlpatterns = [
    # HOME PAGE
    path('', views.home, name='home'),
        # name='home' kwarg (aka an alias)
    # ABOUT PAGE
    path('about/', views.about, name='about'),
    # SKILLS PAGE
    path('skills/', views.skills, name='skills'),
    # PROJECTS PAGE
    path('projects/', views.projects, name='projects'),
    # CONTACT PAGE
    path('contact/', views.contact, name='contact'),
]