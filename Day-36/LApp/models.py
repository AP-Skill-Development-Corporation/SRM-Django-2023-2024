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
	pfimg = models.ImageField(upload_to='Profiles/',default='pfle.png')

class Leave(models.Model):
	y = [
		('s','Select your Leave Type'),
		('Personal','Personal'),
		('Medical','Medical'),
	]
	d = [
		('g','Pending'),
		('a','Approved'),
		('d','Declined'),
	]
	leavetype = models.CharField(choices=y,default='s',max_length=15)
	startdate = models.DateField()
	enddate = models.DateField()
	apldate = models.DateField(auto_now_add=True)
	reason = models.CharField(max_length=200)
	leavestatus = models.CharField(choices=d,default='g',max_length=10)
	tchdesc = models.CharField(max_length=200,blank=False)
	leaatch = models.FileField(upload_to='Attachments/')
	st = models.ForeignKey(User,on_delete=models.CASCADE)

class TchProfile(models.Model):
	tchdesg = models.CharField(max_length=20)
	tchexpr = models.IntegerField()
	tchsubject = models.CharField(max_length=50)
	tchbrnch = models.CharField(max_length=50)
	tstatus = models.BooleanField(default=False)
	tc = models.OneToOneField(User,on_delete=models.CASCADE)

class StProfile(models.Model):
	sbranch = models.CharField(max_length=50)
	syear = models.CharField(max_length=50)
	sstatus = models.BooleanField(default=False)
	sc = models.OneToOneField(User,on_delete=models.CASCADE)



