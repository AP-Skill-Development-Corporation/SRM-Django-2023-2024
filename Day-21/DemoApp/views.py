from django.shortcuts import render
from django.http import HttpResponse

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