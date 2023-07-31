from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class AusForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","eid","role_type"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
		"role_type":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsuserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","eid"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
		}
