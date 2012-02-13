from datetime import datetime

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings

from models import *

urlpatterns = patterns('main.views',
    url(r'^system/$', 'system', name='system'),
    url(r'^new/$', 'new', name='new'),
    url(r'^new/created/$', 'new_created', name='new_created'),
    url(r'^list/page(?P<page>[0-9]+)/$', 'list', name='list_page'),
    url(r'^list/','list', name='list_users'),
    url(r'^download/(?P<tempuserlog_id>[0-9]+)/pdf$', 'download_pdf', name='download_pdf')
)
