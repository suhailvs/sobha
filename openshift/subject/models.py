from django.db import models
from django.contrib import admin
#from openshift.person.models import Teacher

class Grade(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name
			
class Subject(models.Model):
	TYPE_CHOICES = (
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('science', 'Science'),
        ('social', 'Social Studies'),
        ('geography', 'Geography'),
        ('malayalam', 'Malayalam'),
        ('hindi', 'Hindi'),)
	name = models.CharField(max_length=20,choices=TYPE_CHOICES)
	description = models.CharField(max_length=50)
	grade = models.ForeignKey(Grade)
	
	def __unicode__(self):
		return self.name

admin.site.register(Grade)
admin.site.register(Subject)
