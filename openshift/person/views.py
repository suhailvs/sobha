from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login

def students(request):
	errors=[]
	if request.user.is_authenticated():
		return render(request, 'students/pages/home.html')
	
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
    
        
