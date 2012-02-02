# coding: utf-8
import simplejson as json
import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.contrib import messages


from models import *
from forms import *

from pdf import render_to_pdf

def index(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in.
            login(request, form.get_user())
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect( reverse('main.views.system') )
        else:
            form = AuthenticationForm(request)

    return render_to_response('public/index.html', locals(), context_instance=RequestContext(request))

@login_required
def new(request):
    if request.method == "POST":
        form = TempUserForm(data=request.POST)
        if form.is_valid():
            duration = datetime.timedelta(days=form.cleaned_data['duration'])
            expires = datetime.datetime.now() + duration
            log = TempUserLog(
                who=form.cleaned_data['who'],
                why=form.cleaned_data['why'],
                expires=expires,
                issued_by=request.user)
            #TODO : generate username and pasword
            #TODO : save in radiusdb
            log.save()
            messages.success(request, log.id) # Store the id in session, since we are redirecting
            return HttpResponseRedirect( reverse('main.views.new_created') )
        else:
            form = TempUserForm(request.POST)
            return render_to_response('private/new.html', locals(), context_instance=RequestContext(request))
    form = TempUserForm()

    return render_to_response('private/new.html', locals(), context_instance=RequestContext(request))

@login_required
def new_created(request):
    # Retrieve the last id from session
    storage = messages.get_messages(request)
    msgs = [message for message in storage]
    tempuserlog_id = msgs[0].message
    return render_to_response('private/new_created.html', locals(), context_instance=RequestContext(request))


@login_required
def list_users(request):
    # generic view?
    users = TempUserLog.objects.all()
    return render_to_response('private/list.html', locals(), context_instance=RequestContext(request))

@login_required
def system(request):
    return render_to_response('private/system.html', locals(), context_instance=RequestContext(request))


@login_required
def download_pdf(request, tempuserlog_id=-1):
    log = get_object_or_404(TempUserLog, pk=tempuserlog_id)

    return render_to_pdf(
        'pdf/new_temp_user.html',
        {
            'pagesize':'A4',
            'log': log,
        }
    )

def client_status(request):
    # example json view
    data = { 'example' : 'json_view' }
    return HttpResponse(json.dumps(data), content_type='application/javascript; charset=utf8')

