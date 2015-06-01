from django.conf.urls import patterns, include, url
from survey import urls as appurls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SurveySite.views.home', name='home'),
    # url(r'^SurveySite/', include('SurveySite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include(appurls)),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
