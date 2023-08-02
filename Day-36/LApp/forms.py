from .models import User,TchProfile,StProfile,Leave
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
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

class StpForm(forms.ModelForm):
	class Meta:
		model = StProfile
		fields = ["sbranch","syear"]
		widgets = {
		"sbranch":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Branch",
			}),
		"syear":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Year",
			}),
		}

class LeavForm(forms.ModelForm):
	class Meta:
		model = Leave
		fields = ["leavetype","startdate","enddate","leaatch","reason"]
		widgets = {
		"leavetype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"startdate":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"enddate":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"reason":forms.Textarea(attrs={
			"class":"form-control my-2",
			"rows":3,
			})
		}

class UpleaForm(forms.ModelForm):
	class Meta:
		model = Leave
		fields = ["leavetype","leavestatus","tchdesc"]
		widgets = {
		"leavetype":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"leavestatus":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"tchdesc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"rows":"3",
			}),
		}

class ChgPwdForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = "__all__"