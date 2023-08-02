from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('lgn/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
	path('usrlst/',views.userlist,name="usrl"),
	path('pfle/',views.profile,name="pf"),
	path('upfle/',views.updprofile,name="upf"),
	path('lvst/',views.leavelist,name="lvs"),
	path('tclvlst/',views.tchlevlst,name="tclst"),
	path('upl/<int:h>/',views.upleav,name="uplv"),
	path('updlv/<int:w>/',views.upstleave,name="upls"),
	path('dleusr/<int:p>/',views.lvdlt,name="dlu"),
	path('chge/',views.chgepwd,name="cge"),
]