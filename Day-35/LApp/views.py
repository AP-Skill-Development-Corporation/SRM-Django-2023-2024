from django.shortcuts import render,redirect
from .forms import AusForm,UsuserForm,UspForm,TchprForm
from django.contrib import messages
from .models import User,TchProfile

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
	h = TchProfile.objects.get(tc_id=request.user.id)
	g = User.objects.get(id=request.user.id)
	d = {}
	d[0] = h.tchdesg
	d[1] = h.tchexpr
	d[2] = h.tchsubject
	d[3] = h.tchbrnch
	d[4] = h.tc_id
	return render(request,'html/profile.html',{'j':d})

def updprofile(request):
	k = User.objects.get(id=request.user.id)
	if request.user.role_type == "2":
		t = TchProfile.objects.all()
		m = []
		for i in t:
			m.append(i.tc_id)
		if request.user.id not in m:
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				y = TchprForm(request.POST)
				if h.is_valid() and y.is_valid():
					h.save()
					b = y.save(commit=False)
					b.tc_id=request.user.id
					b.save()
					return redirect('/pfle')
			y = TchprForm()
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})
		else:
			p = TchProfile.objects.get(tc_id=request.user.id)
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				y = TchprForm(request.POST)
				if h.is_valid() and y.is_valid():
					h.save()
					b.save()
					return redirect('/pfle')
			y = TchprForm(instance=p)
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})	
	elif request.user.role_type == "1":
		if request.method == "POST":
			h = UspForm(request.POST,request.FILES,instance=k)
			if h.is_valid():
				h.save()
				return redirect('/pfle')
		h = UspForm(instance=k)
		return render(request,'html/updateprofile.html',{'e':h})
	else:
		if request.method == "POST":
			h = UspForm(request.POST,request.FILES,instance=k)
			if h.is_valid():
				h.save()
				return redirect('/pfle')
		h = UspForm(instance=k)
		return render(request,'html/updateprofile.html',{'e':h})