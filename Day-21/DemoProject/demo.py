from django.http import HttpResponse

def dy(request,ty,ag):
	return HttpResponse(f"Welcome User <span style='color:red'>{ty}</span><br>Age is: {ag}")