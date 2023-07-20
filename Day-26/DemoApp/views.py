from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import EmForm

# Create your views here.
def sample(s):
	return HttpResponse("Good Evening")

def demo(request,y):
	return HttpResponse(f"Good Afternoon {y}")

def studentdetails(request,ag,rn,sname):
	return HttpResponse(f"Student Details are:<br> Roll Number: {rn}<br> Student Name: {sname}<br> Age is: {ag}")

def demoprint(request,nme):
	return HttpResponse(f"<h4>Welcome User <span>{nme}</span></h4>")

def dy(request,ty,ag):
	return HttpResponse(f"<h4>Welcome User <span style='color:red'>{ty}</span><br>Age is: {ag}</h4>")

def jasv(request,tw):
	return HttpResponse(f"<script>alert('Hi User {tw}')</script>Hi {tw}")

def ht(request):
	return render(request,'demo.html')

def fer(s):
	return render(s,'firstapp/demopage.html')

def dsply(request,jk,a):
	return render(request,'firstapp/first.html',{'nm':jk,'ag':a})

def student(request):
	if request.method == "POST":
		a = request.POST['rn']
		b = request.POST['sn']
		c = request.POST['em']
		d = request.POST['ag']
		return render(request,'firstapp/display.html',{'roll':a,"sname":b,"mal":c,"age":d})	
	return render(request,'firstapp/stform.html')

def boot(request):
	return render(request,'firstapp/bt.html')

def regform(request):
	return render(request,'firstapp/register.html')

def exfls(request):
	return render(request,'firstapp/gt.html')

def btsdsn(request):
	return render(request,'firstapp/bootstapdesign.html')

def crud(request):
	t = Student.objects.all()
	if request.method == "POST":
		a = request.POST['r']
		b = request.POST['s']
		c = request.POST['y']
		d = request.POST['b']
		w = Student.objects.create(roll=a,sname=b,year=c,branch=d)
		return redirect('/')
	return render(request,'firstapp/crud.html',{'v':t})

def stup(request,s):
	z = Student.objects.get(id=s)
	if request.method == "POST":
		z.sname = request.POST['s']
		z.year = request.POST['y']
		z.branch = request.POST['b']
		z.save()
		return redirect('/')
	return render(request,'firstapp/stupdate.html',{'t':z})

def stdlt(request,p):
	n = Student.objects.get(id=p)
	if request.method == "POST":
		n.delete()
		return redirect('/')
	return render(request,'firstapp/stdelete.html',{'z':n})

def employee(request):
	g = EmForm()
	return render(request,'firstapp/employeelist.html',{'k':g})