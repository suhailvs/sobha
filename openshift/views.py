from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import RequestContext

def guest_hnav_main(request):
	hnav=[('/home/','Home'),
		('/aboutus/','About us'),
		('/admission/','Admission'),
		('/develop/','Develop this site'),
		('/activities/','Activities'),
		('/career/','Career'),
		('/contactus/','Contact us'),
		('/gmaps/','Map of school')]

	return {
        'nav_items': hnav,
    }

def menulinks(request,template_name):
	cur_page='/%s/'%template_name[:-5]
	return render(request,'guest/pages/%s'%(template_name,),{'cur_page':cur_page},
	context_instance=RequestContext(request,processors=[guest_hnav_main]))




	    	