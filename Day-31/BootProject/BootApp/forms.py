from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		}