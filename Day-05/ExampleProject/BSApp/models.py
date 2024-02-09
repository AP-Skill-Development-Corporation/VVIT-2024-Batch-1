from django.db import models

# Create your models here.

class Student(models.Model):
	rn = models.CharField(max_length=12)
	sn = models.CharField(max_length=150)
	sy = models.IntegerField(default=18)


class Employee(models.Model):
	y = [
		('0','-- Select Designation --'),
		('1','Intern'),
		('2','Junior Trainee'),
		('3','Junior Developer'),
	]
	eid = models.CharField(max_length=10)
	ename = models.CharField(max_length=20)
	esal = models.CharField(max_length=10)
	edesg = models.CharField(choices=y,default='0',max_length=5)
	
	def __str__(self):
		return self.ename
