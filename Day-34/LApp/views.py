from django.shortcuts import render,redirect
from .forms import AusForm,UsuserForm
from django.contrib import messages
from .models import User

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		f = UsuserForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request,"User Created Successfully")
			return redirect('/lgn')
	else:
		f = UsuserForm()
	return render(request,'html/register.html',{'g':f})

def userlist(request):
	c = User.objects.all()
	n,m = {},{}
	if request.method == "POST":
		s = AusForm(request.POST)
		if s.is_valid():
			s.save()
			messages.success(request,'User Created Successfully')
			return redirect('/usrlst')
		else:
			n[s] = s.errors
	for j in n.values():
		for v in j.items():
			m[v[0]] = v[1]
	s = AusForm()
	return render(request,'html/userlist.html',{'w':s,'p':m.items(),'k':c})

def profile(request):
	return render(request,'html/profile.html')