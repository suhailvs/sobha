from django.db import models
from django.contrib import admin
# Create your models here.
from openshift.subject.models import Grade,Subject

class Person(models.Model):	
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20,blank=True)
	dob = models.DateField(blank=True)
	phone = models.IntegerField(max_length=15,blank=True)
	TYPE_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),)
	sex = models.CharField(max_length=6,choices=TYPE_CHOICES)
	pincode = models.IntegerField(max_length=6,blank=True)
	address = models.CharField(max_length=80,blank=True)
	
	def __unicode__(self):
		return u'%s %s' % (self.fname, self.lname)

class Parent(models.Model):
	person =  models.ForeignKey(Person)
	TYPE_CHOICES = (
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),)
	relationship = models.CharField(max_length=10,choices=TYPE_CHOICES)
	def __unicode__(self):
		return self.person.fname
		
class Student(models.Model):
	person =  models.ForeignKey(Person)
	parent =  models.ForeignKey(Parent)
	#classroom =  models.ForeignKey(Classroom)
	date_of_join = models.DateField(blank=True)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.person.fname

class StudentAdmin(admin.ModelAdmin):
    list_display = ('person', 'parent')#,'classroom')
	
class Staff(models.Model):
	person =  models.ForeignKey(Person)
	TYPE_CHOICES = (
        ('cook', 'Cook'),
        ('servant', 'Servant'),
        ('teacher', 'Teacher'),
		('peon', 'Peon'),
        ('constructor', 'Construction worker'),
        ('clerk', 'Clerk'),
        ('other', 'Others'),
        ) 
	nature_of_job = models.CharField(max_length=15,choices=TYPE_CHOICES)
	basic_pay = models.IntegerField(max_length=6,blank=True)
	date_of_join = models.DateField(blank=True)
	def __unicode__(self):
		return self.person.fname
	
class Teacher(models.Model):
	staff =  models.ForeignKey(Staff)
	subjects = models.ManyToManyField(Subject)
	status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.staff.person.fname
		
class Classroom(models.Model):
	grade = models.ForeignKey(Grade)
	teacher = models.ForeignKey(Teacher) 
	location = models.CharField(max_length=30)
	status = models.BooleanField(default=True)
	remarks = models.CharField(max_length=50)
	def __unicode__(self):
		return self.grade.name

class Attendance(models.Model):
	person =  models.ForeignKey(Person)
	date = models.DateField()
	status = models.BooleanField(default=True)
	remark = models.CharField(max_length=50)
	def __unicode__(self):
		return self.person.fname
		
admin.site.register(Person)
admin.site.register(Parent)
admin.site.register(Student,StudentAdmin)
admin.site.register(Staff)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Attendance)
