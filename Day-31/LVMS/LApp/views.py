from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	return render(request,'html/register.html')