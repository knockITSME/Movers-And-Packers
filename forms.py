from django import forms
from PM.models import userdetails

class FormUserdetails(forms.ModelForm):
  class Meta:
   model=userdetails
   fields=["username","usercontact","useremail","userpassword"]