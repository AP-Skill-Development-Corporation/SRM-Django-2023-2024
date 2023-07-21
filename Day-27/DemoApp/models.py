from django.db import models

# Create your models here.
class Student(models.Model):
	roll = models.CharField(max_length=15)
	sname = models.CharField(max_length=30)
	year = models.IntegerField()
	branch = models.CharField(max_length=30)

class Employee(models.Model):
	t = [
		('0','Select Your Designation'),
		('1','Junior Trainee'),
		('2','Senior Trainee'),
		('3','Manager'),
	]
	eid = models.CharField(max_length=15)
	ename = models.CharField(max_length=30)
	edesgn = models.CharField(max_length=20,choices=t,default='0')
	eage = models.IntegerField(default=20)
	eexprew = models.CharField(max_length=200)