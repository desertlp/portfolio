from django.db import models

TYPES = (
  ('lang','Language'),
  ('frmwk', 'Framework'),
  ('db','Database'),
  ('styl','Styling'),
)

class Project(models.Model):
    name = models.CharField(max_length=100)
    project_url = models.URLField(max_length=250)
    # CharField uses a <input type="text"> as its widget, whereas, a TextField uses a <textarea>
    description = models.TextField(max_length=500)
    deployment_date = models.DateField()
        # format should be YYYY-MM-DD

    def __str__(self):
        return self.name 

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
        return self.name 
            # Nice method for obtaining the friendly value of a Field.choice