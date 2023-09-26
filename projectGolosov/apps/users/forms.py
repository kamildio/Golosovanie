from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)
    birthdate = forms.DateField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "birthdate")

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'birthdate', 'image', 'isCandit']