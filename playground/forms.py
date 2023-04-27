from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Doctor

# Create your models here.
class signup_form_doc (forms.ModelForm):
    
    class Meta:
        model=Doctor
        widgets={'password':forms.PasswordInput()}
        fields=('email_id','first_name','last_name','nmc_id','state','year','password')