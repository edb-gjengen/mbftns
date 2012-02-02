from datetime import datetime

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list_detail import object_list # FIXME: subclass?
from django.contrib.auth.decorators import login_required

from models import *

urlpatterns = patterns('main.views',
    url(r'^system/$', 'system', name='system'),
    url(r'^new/$', 'new', name='new'),
    url(r'^new/created/$', 'new_created', name='new_created'),
    url(r'^list/page(?P<page>[0-9]+)/$',
        login_required(object_list), {
            'queryset': TempUserLog.objects.filter(expires__gte=datetime.now()).order_by('created').reverse(),
            'template_name':'private/list.html'
        }, name='list_page'),
    url(r'^list/',
        login_required(object_list), {
            'queryset': TempUserLog.objects.filter(expires__gte=datetime.now()).order_by('created').reverse(),
            'template_name':'private/list.html'
        },
        name='list_users'),
    url(r'^download/(?P<tempuserlog_id>[0-9]+)/pdf$', 'download_pdf', name='download_pdf')
)
