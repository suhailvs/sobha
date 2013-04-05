from django.db import models
from django.contrib import admin
# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=40)
	subject = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	message = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now_add=True)


class ContactAdmin(admin.ModelAdmin):
	list_display = ["name", "subject", "created"]
	search_fields = ["name"]


admin.site.register(Contact,ContactAdmin)

