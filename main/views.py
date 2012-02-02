# coding: utf-8
import simplejson as json

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from models import *

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
    return render_to_response('private/new.html', locals(), context_instance=RequestContext(request))

@login_required
def system(request):
    return render_to_response('private/system.html', locals(), context_instance=RequestContext(request))


@login_required
def download_pdf(request):
    # TODO Retrieve data
    results = [1,2,3,4,5,'lol'] 
    return render_to_pdf(
        'pdf/new_temp_user.html',
        {
            'pagesize':'A4',
            'mylist': results,
        }
    )

def client_status(request):
    # example json view
    data = { 'example' : 'json_view' }
    return HttpResponse(json.dumps(data), content_type='application/javascript; charset=utf8')

