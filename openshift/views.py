from django.shortcuts import render
from openshift import templatehelper
from django.contrib.auth.models import User

hnav=templatehelper.getmenu()
def menulinks(request,template_name):
	cur_page='/%s/'%template_name[:-5]	
	return render(request,'guest/pages/%s'%(template_name,),{'cur_page':cur_page,'nav_items':hnav})


from django.contrib.auth import authenticate, login

def signin(request):
	errors=[]
	if request.method == 'POST':		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to a success page.
				return render(request, 'students/pages/home.html')
			else:
				errors.append('disabled account')
		else:
			errors.append("The username and password were incorrect.")
	return render(request, 'guest/pages/signin.html',{'errors': errors})
	    	
def studentadmin(request):
	pass