from django.db import models

# Create your models here.
from django.contrib import admin
from openshift.person.models import Classroom, Student
from openshift.subject.models import Subject

class ExamType(models.Model):
	TYPE_CHOICES = (
        ('onam', 'Onam'),
        ('christmas', 'Christmas'),
        ('annual', 'Annual'),
        )
	name = models.CharField(max_length=20,choices=TYPE_CHOICES)
	description = models.CharField(max_length=50,blank=True)	
	def __unicode__(self):
		return self.name

class Exam(models.Model):
	examtype=  models.ForeignKey(ExamType)
	start_date = models.DateField()
	def __unicode__(self):
		return self.examtype.name

class ExamResult(models.Model):
	student =  models.ForeignKey(Student)
	exam = models.ForeignKey(Exam)
	subject =  models.ForeignKey(Subject)
	max_mark = models.IntegerField(max_length=3)
	pass_mark =	models.IntegerField(max_length=3)
	mark_obt = models.IntegerField(max_length=3)
	duration = models.IntegerField(max_length=3)#minutes
	result = models.BooleanField(default=True)
	def __unicode__(self):
		return self.student.person.fname

class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('mark_obt','max_mark','result')
    
class ExamTimetable(models.Model):
	exam = models.ForeignKey(Exam)
	subject =  models.ForeignKey(Subject)
	start_time =  models.DateTimeField()
	duration = models.IntegerField()
	def __unicode__(self):
		return self.subject.name

admin.site.register(ExamType)
admin.site.register(Exam)
admin.site.register(ExamTimetable)
admin.site.register(ExamResult,ExamResultAdmin)
