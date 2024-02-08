from django.db import models

# Create your models here.

class Student(models.Model):
	rn = models.CharField(max_length=12)
	sn = models.CharField(max_length=150)
	sy = models.IntegerField(default=18)

	
