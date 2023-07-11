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