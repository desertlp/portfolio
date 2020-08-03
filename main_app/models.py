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
        return f"{self.get_skill_type_display()}"


class Project(models.Model):
    name = models.CharField(max_length=100)
    project_url = models.URLField(max_length=250)
    # CharField uses a <input type="text"> as its widget, whereas, a TextField uses a <textarea>
    description = models.TextField(max_length=500)
    deployment_date = models.DateField()
        # format should be YYYY-MM-DD
    # Create a skill_id FK
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
        # ForeignKey field-type is used to create a one-to-many relationship.
        # Since a project belong to a skill set, project must hold the id of the skill object it belongs to, aka foreign key

    def __str__(self):
        return self.name 





