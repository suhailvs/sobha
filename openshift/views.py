from django.shortcuts import render
import os
from openshift import templatehelper
		
hnav=templatehelper.getmenu()
def home(request):	
	return render(request,'pages/home.html',{'cur_page':'/home/','nav_items':hnav})
def aboutus(request):
	return render(request,'pages/aboutus.html',{'cur_page':'/aboutus/','nav_items':hnav})
def admission(request):	
	return render(request,'pages/admission.html',{'cur_page':'/admission/','nav_items':hnav})
def develop(request):
	return render(request,'pages/develop.html',{'cur_page':'/explore/','nav_items':hnav})
def activities(request):	
	return render(request,'pages/activities.html',{'cur_page':'/activities/','nav_items':hnav})
def career(request):	
	return render(request,'pages/career.html',{'cur_page':'/career/','nav_items':hnav})
def contactus(request):
	return render(request,'pages/contactus.html',{'cur_page':'/contactus/','nav_items':hnav})
def schoolmap(request):	
	return render(request,'pages/schoolmap.html',{'cur_page':'/gmaps/','nav_items':hnav})
	

	

