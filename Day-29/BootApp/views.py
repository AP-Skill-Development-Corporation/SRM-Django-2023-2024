from django.shortcuts import render,redirect
from .forms import UserForm

# Create your views here.
def home(request):
	return render(request,'ht/home.html')

def about(request):
	return render(request,'ht/about.html')

def contact(request):
	return render(request,'ht/contact.html')

def register(request):
	if request.method == "POST":
		r = UserForm(request.POST)
		if r.is_valid():
			r.save()
			return redirect('/')	
	r = UserForm()
	return render(request,'ht/register.html',{'d':r})