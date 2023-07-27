from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	g = [
		('0','--- Select Your Gender ---'),
		('1','Male'),
		('2','Female'),
	]
	c = [
		('0','Guest'),
		('1','Student'),
		('2','Teacher'),
	]
	mble = models.CharField(max_length=10,null=True,blank=True)
	gdr = models.CharField(choices=g,default='0',max_length=5)
	role_type = models.CharField(choices=c,default='0',max_length=5)
	eid = models.CharField(max_length=10)

