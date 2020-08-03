from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('skills/<int:skill_id>/', views.skill_projects, name='skill_projects'),
      # skills / = resource <int:skill_id>=id views.skill_projects= a method
      # skill_id> can be anything, pizza variable, but try to make it sematic
      # The int: part is called a converter and it's used to match and convert the captured value from a string into, in this case, an integer. If the info in the segment does not look like an integer, then it will not be matched - this is different than what we saw in Express where the type of info in a segment didn't matter.
    # Projects Page
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]