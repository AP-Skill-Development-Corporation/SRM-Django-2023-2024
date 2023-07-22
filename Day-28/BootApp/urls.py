from django.urls import path
from BootApp import views

urlpatterns = [
	path('',views.home,name="hm"),
]