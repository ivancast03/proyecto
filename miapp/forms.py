from django import forms
from .models import Dork
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class DorkForm(forms.ModelForm):
    class Meta:
        model = Dork
        fields = ["titulo", "dork"]

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingrese una dirección de correo válida.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)