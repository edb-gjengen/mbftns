#!/usr/bin/env python
# coding: utf-8
import os
import sys
from datetime import datetime

project_path = '/var/www/neuf.no/mbftns/mbftns/'
if project_path not in sys.path:
    sys.path.append(project_path)

from django.core.management import setup_environ
from django.core.mail import mail_admins
import settings

setup_environ(settings)

from main.models import *
from radius.models import *
# Find expired userpass objects, format into a list.
# Then use the id's in an inner query to delete them
# Note: Use this way of referencing since UserPass and Radcheck objects are in different DBs
up_ids = UserPass.objects.filter(log__expires__lte=datetime.now()).values_list('radcheck_id', flat=True)
Radcheck.objects.filter(id__in=list(up_ids)).delete()
