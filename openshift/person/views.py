from django.shortcuts import render
# Create your views here.


def studentadmin(request):
	if not request.user.is_authenticated():
		return render(request, 'guest/pages/signin.html')
	
	return render(request,'student/pages/home.html')
    
        