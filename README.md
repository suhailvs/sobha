Sobha on openshift
==================

Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/

Install git and ruby

Install the RHC client tools if you have not already done so:
    
    sudo gem install rhc

Create a python-2.6 application

    rhc app create -a django -t python-2.6

Add openshift/django-example upstream repo

    cd django
    git remote add upstream -m master git://github.com/openshift/django-example.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

As the `git push` output scrolls by, keep an eye out for a
line of output that starts with `CLIENT_MESSAGE: `. This line
contains the generated admin password that you will need to begin
administering your Django app. This is the only time the password
will be displayed, so be sure to save it somewhere.
	
That's it. You can now checkout your application at:

    http://django-$yournamespace.rhcloud.com



How to frequent update site
---------------------------

go to the folder django(created when *rhc app create -a django -t python-2.6* command called):

	cd django

make changes using your favourate text editor. replace the folder *wsgi/openshift* with this repository foler:
	
	git add .
	git commit -a
	git push
	

	
othe rhc commands
-----------------


to list all apps:

	rhc apps
	
to delete app:
	
	rhc app delete sobha --confirm