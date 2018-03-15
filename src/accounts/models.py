from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	gender_choice =(
		('Male','Male'),
		('Female','Female'),
		)
	is_student     = models.BooleanField('student status', default=False)
	is_teacher     = models.BooleanField('teacher status', default=False)
	avatar         = models.ImageField(null=True ,blank=True)
	birth_day      = models.DateField(null=True,blank=True)
	birth_location = models.CharField(max_length=30, null=True ,blank=True)
	adresse        = models.CharField(max_length=30, null=True ,blank=True)
	gender         = models.CharField(max_length=6,choices=gender_choice,)

class Student(models.Model):
	user      = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='students')
	classroom = models.ForeignKey('Grade', default=1)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name



class Teacher(models.Model):
	reciption_choice =(
		('Sunday','Sunday'),
		('Monday','Monday'),
		('Tuseday','Tuseday'),
		('Wednesday','Wednesday'),
		('Thursday','Thursday'),
		)
	user      = models.OneToOneField(User,on_delete=models.CASCADE, related_name='teachers')
	classroom = models.ManyToManyField('Grade',)
	module    = models.ForeignKey('Module',)
	reciption = models.CharField(max_length=10,choices=reciption_choice, null=True)
	

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name



class Grade(models.Model):
	name = models.CharField(max_length=5,null=True)

	def __str__(self):
		return self.name 


class Module (models.Model):
	module_choice =(
		('Arabic','Arabic'),
		('English','English'),
		('French','French'),
		('Sport','Sport'),
		)
	name    = models.CharField(max_length=10,choices=module_choice, null=True)


	def __str__(self):
		return self.name




