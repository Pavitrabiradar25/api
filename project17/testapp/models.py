from django.db import models

# Create your models here

class Student(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone_num = models.IntegerField()
	address = models.CharField(max_length=50)
