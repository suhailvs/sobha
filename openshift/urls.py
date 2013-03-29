from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('openshift',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    url(r'^home/$', 'views.home', name='home'),
    url(r'^aboutus/$','views.aboutus'),
    url(r'^admission/$','views.admission'),
    url(r'^develop/$','views.develop'),
    url(r'^activities/$','views.activities'),
    url(r'^career/$','views.career'),
    url(r'^contactus/$','views.contactus'),
    url(r'^gmaps/$','views.schoolmap'),
    #url(r'^search/$','students.views.search'),
    #url(r'^search_student/$','students.views.search'),
    url(r'^admin/', include(admin.site.urls)),
)
