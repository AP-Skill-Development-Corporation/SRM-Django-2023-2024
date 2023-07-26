from django.shortcuts import render,redirect
from .forms import UserForm
from BootProject import settings
from django.core.mail import send_mail
from django.contrib import messages
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

def mailsending(request):
	if request.method == "POST":
		sndr = request.POST['sn']
		sbj = request.POST['sb']
		m = request.POST['msg']
		t = settings.EMAIL_HOST_USER
		b = send_mail(sbj,m,t,[sndr])
		if b == 1:
			messages.success(request,"Mail sent Successfully")
			return redirect('/mail')
		else:
			messages.error(request,"Mail not Sent")
			return redirect('/mail')
	return render(request,'ht/mail.html')