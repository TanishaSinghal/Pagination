from django import forms
from .models import *

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class user_data(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    name = forms.CharField(max_length = 255)
    email = forms.EmailField(max_length = 255)
    
    class Meta:
        model = Users
        fields = "__all__"
        