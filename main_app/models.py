from django.db import models

TYPES = (
  ('lang','Language'),
  ('frmwk', 'Framework'),
  ('db','Database'),
  ('styl','Styling'),
)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_type = models.CharField(
        'Skill Type',
        # Adds a drop down for skill_type option (language, framework, tool, special)
        max_length = 100,
        choices=TYPES,
            # Sets enumerater option for skill_type choices from tuples 
        # Set Default Type
        default=TYPES[0][0],
            # default to language 
    )
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    project_url = models.URLField(max_length=250)
    # CharField uses a <input type="text"> as its widget, whereas, a TextField uses a <textarea>
    description = models.TextField(max_length=500)
    deployment_date = models.DateField()
        # format should be YYYY-MM-DD
    # Create a skill_id FK
    skill = models.ForeignKey(Skill, default="", on_delete=models.CASCADE)
        # ForeignKey field-type is used to create a one-to-many relationship.
        # Since a project belong to a skill set, project must hold the id of the skill object it belongs to, aka foreign key
        # on_delete=models.CASCADE is required. It ensures that if a Cat record is deleted, all of the child Feedings will be deleted automatically as well - thus avoiding orphan records 
    def __str__(self):
        return self.name 



class Contact(models.Model): 
    first_name = models.CharField('First', max_length=50)
    last_name = models.CharField('Last', max_length=50)
    company = models.CharField(max_length=100, default="")
    email = models.EmailField('email', max_length=150)
        # https://docs.djangoproject.com/en/2.2/ref/validators/#django.core.validators.EmailValidator
    message = models.TextField(max_length=500, default="")
    submition_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

