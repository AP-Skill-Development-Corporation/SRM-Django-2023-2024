from .models import User,TchProfile
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

class UspForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","mble","gdr","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"gdr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class TchprForm(forms.ModelForm):
	class Meta:
		model = TchProfile
		fields = ["tchbrnch","tchsubject","tchdesg","tchexpr"]
		widgets = {
		"tchbrnch":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Branch",
			}),
		"tchsubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Subject",
			}),
		"tchdesg":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Designation",
			}),
		"tchexpr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		}