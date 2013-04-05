from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('openshift',
 url(r'^admin/', include(admin.site.urls)),
 url(r'^contactus/$','contact.views.contactus'),
 url(r'^student/$','person.views.studentadmin'),
 )
 
 
urlpatterns += patterns('openshift.views',
    url(r'^$', 'menulinks', {'template_name': 'home.html'}),
    url(r'^home/$', 'menulinks', {'template_name': 'home.html'}),
    url(r'^aboutus/$','menulinks', {'template_name': 'aboutus.html'}),
    url(r'^admission/$','menulinks', {'template_name': 'admission.html'}),
    url(r'^develop/$','menulinks', {'template_name': 'develop.html'}),
    url(r'^activities/$','menulinks', {'template_name': 'activities.html'}),
    url(r'^career/$','menulinks', {'template_name': 'career.html'}),    
    url(r'^gmaps/$','menulinks', {'template_name': 'gmaps.html'}),   
    url(r'^signin/$','signin'), 
)
