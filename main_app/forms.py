from django import forms
from .models import Contact

# Feeding Form
class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['first_name', 'last_name', 'company', 'email', 'message']
            # arguments must match fields of Contact model
            # do not need submition date bc it is a non-editable field
            
# form inherits from ModelForm and has a nested class Meta: to declare the Model being used and the fields we want inputs generated for. Confusing? Absolutely, but it's just the way it is, so accept it and sleep well