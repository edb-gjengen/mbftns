from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    url(r'^accounts/login', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout'),
)
# for dev
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()
