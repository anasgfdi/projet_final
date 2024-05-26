from django import forms

from signup.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
   class Meta:
     model = User
     fields = '__all__'

class UserCreationFormCustom(UserCreationForm):
  class Meta(UserCreationForm):
         fields = '__all__'

