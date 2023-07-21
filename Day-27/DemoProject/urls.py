"""DemoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DemoApp import views
# from DemoProject import demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('st/',views.sample),
    path('t/<str:y>/',views.demo),
    path('stu/<str:rn>/<str:sname>/<int:ag>/',views.studentdetails),
    path('py/<str:nme>/',views.demoprint),
    path('k/<str:ty>/<int:ag>/',views.dy),
    path('mk/<str:tw>/',views.jasv),
    path('ty/',views.ht),
    path('pyy/',views.fer),
    path('er/<str:jk>/<int:a>/',views.dsply),
    path('std/',views.student),
    path('y/',views.boot),
    path('dy/',views.regform),
    path('kp/',views.exfls),
    path('ety/',views.btsdsn),
    path('styu/',views.crud,name="cru"),
    path('stp/<int:s>/',views.stup,name="stpd"),
    path('stdt/<int:p>/',views.stdlt,name="std"),
    path('',views.employee,name="emp"),
    path('empu/<int:h>/',views.empupdate,name="empup"),
]
