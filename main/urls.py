from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^system/', 'system'),
    url(r'^new/', 'new'),
    url(r'^list/', 'list_users'),
)
