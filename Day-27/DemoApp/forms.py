from .models import Employee
from django import forms

class EmForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["eid","ename","eage","edesgn","eexprew"]
		widgets = {
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Id",
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Name",
			}),
		"eage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Age",
			"max":70,
			"min":19,
			}),
		"edesgn":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"eexprew":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Review",
			"rows":3,
			})
		}