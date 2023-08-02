from django.shortcuts import render,redirect
from .forms import AusForm,UsuserForm,UspForm,TchprForm,StpForm,LeavForm,UpleaForm,ChgPwdForm
from django.contrib import messages
from .models import User,TchProfile,StProfile,Leave

# Create your views here.
def home(request):
	if request.user.role_type == "1":
		s = Leave.objects.filter(st_id=request.user.id)
		return render(request,'html/home.html',{'st':s})
	elif request.user.role_type == "2":
		v = TchProfile.objects.get(id=request.user.id)
		c = StProfile.objects.all()
		g,m,p = {},{},{}
		for i in c:
			if i.sbranch == v.tchbrnch:
				g[i.sc_id] = i.syear
		q = User.objects.all()
		for k in q:
			if k.id in g:
				q = Leave.objects.filter(st_id=k.id).count()
				pp = Leave.objects.filter(st_id=k.id,leavestatus='g').count()
				ff = Leave.objects.filter(st_id=k.id,leavestatus='a').count()
				m[k.id] = k.username,g[k.id],k.pfimg,q,pp,ff,q-(pp+ff)
		return render(request,'html/home.html',{'tc':m.values()})
	else:
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
					b.tstatus = 1
					b.save()
					return redirect('/pfle')
			y = TchprForm()
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})
		else:
			p = TchProfile.objects.get(tc_id=request.user.id)
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				y = TchprForm(request.POST,instance=p)
				if h.is_valid() and y.is_valid():
					h.save()
					y.save()
					return redirect('/pfle')
			y = TchprForm(instance=p)
			h = UspForm(instance=k)
			return render(request,'html/updateprofile.html',{'e':h,'t':y})	
	elif request.user.role_type == "1":
		j = StProfile.objects.all()
		s = []
		for i in j:
			s.append(i.sc_id)
		if request.user.id not in s:
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				n = StpForm(request.POST)
				if h.is_valid() and n.is_valid():
					h.save()
					z = n.save(commit=False)
					z.sc_id = request.user.id
					z.sstatus = 1
					z.save()
					return redirect('/pfle')
			h = UspForm(instance=k)
			n = StpForm()
			return render(request,'html/updateprofile.html',{'e':h,'a':n})
		else:
			v = StProfile.objects.get(sc_id=request.user.id)
			if request.method == "POST":
				h = UspForm(request.POST,request.FILES,instance=k)
				n = StpForm(request.POST,instance=v)
				if h.is_valid() and n.is_valid():
					h.save()
					n.save()
					return redirect('/pfle')
			h = UspForm(instance=k)
			n = StpForm(instance=v)
			return render(request,'html/updateprofile.html',{'e':h,'a':n})
	else:
		if request.method == "POST":
			h = UspForm(request.POST,request.FILES,instance=k)
			if h.is_valid():
				h.save()
				return redirect('/pfle')
		h = UspForm(instance=k)
		return render(request,'html/updateprofile.html',{'e':h})

def leavelist(request):
	p = Leave.objects.filter(st_id = request.user.id)
	if request.method == "POST":
		d = LeavForm(request.POST,request.FILES)
		if d.is_valid():
			w = d.save(commit=False)
			w.st_id = request.user.id
			w.save()
			return redirect('/lvst')
	d = LeavForm()
	return render(request,'html/leavelist.html',{'z':d,'h':p})

def tchlevlst(request):
	y = User.objects.filter(role_type='1')
	f = TchProfile.objects.get(tc_id=request.user.id)
	r,p,m = {},{},{}
	for i in y:
		r[i.id] = i.username
	k = StProfile.objects.all()
	for j in k:
		if j.sc_id in r and j.sbranch == f.tchbrnch:
			p[j.sc_id] = j.syear,r[j.sc_id]
	for z in p:
		q = Leave.objects.filter(st_id=z)
		for v in q:
			m[v.id] = v.leavetype,v.apldate,v.leavestatus,p[v.st_id][1],p[v.st_id][0],v.id
	return render(request,'html/teacherlist.html',{'t':m.values()})

def upleav(request,h):
	b = Leave.objects.get(id=h)
	if request.method == "POST":
		g = UpleaForm(request.POST,instance=b)
		if g.is_valid():
			g.save()
			return redirect('/tclvlst')
	g = UpleaForm(instance=b)
	return render(request,'html/updeleave.html',{'v':g})

def upstleave(request,w):
	z = Leave.objects.get(id=w)
	if request.method == "POST":
		x = LeavForm(request.POST,instance=z)
		if x.is_valid():
			x.save()
			return redirect('/lvst')
	x = LeavForm(instance=z)
	return render(request,'html/uplstleave.html',{'c':x})

def lvdlt(request,p):
	k = Leave.objects.get(id=p)
	if request.method == "POST":
		k.delete()
		return redirect('/lvst')
	return render(request,'html/deleave.html',{'a':k})

def chgepwd(request):
	if request.method == "POST":
		n = ChgPwdForm(user=request.user,data=request.POST)
		if n.is_valid():
			n.save()
			return redirect('/lgn')
	n = ChgPwdForm(user=request)
	return render(request,'html/changepaswd.html',{'h':n})