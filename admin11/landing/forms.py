from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

from .models import *

class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'123'}))
	email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'123'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'123'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'123'}))

	class Meta:
		model = User
		fields = ('username','email','password1','password2')
		# widgets = {
		# 	'username': forms.TextInput(attrs={'class':'from-input'}),
		# 	'password1': forms.PasswordInput(attrs={'class':'from-input'}),
		# 	'password2': forms.PasswordInput(attrs={'class':'from-input'})
		# }