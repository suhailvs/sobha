# Create your views here.
from django.shortcuts import render

from openshift.contact.form import ContactForm
from openshift.contact.models import Contact
from django.template import RequestContext
from openshift.views import guest_hnav_main

def contactus(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			cd = form.cleaned_data
			c1=Contact(name=cd['name'],subject=cd['subject'],email=cd['email'],message=cd['message'])
			c1.save()

			return render(request,'guest/contact/success.html',{'cur_page':'/contactus/'},context_instance=RequestContext(request,processors=[guest_hnav_main]))
	else:
		form=ContactForm()
	return render(request,'guest/contact/contact.html',{'cur_page':'/contactus/','form':form},context_instance=RequestContext(request,processors=[guest_hnav_main]))
