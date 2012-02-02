#!/usr/bin/env python
# coding: utf-8
import os
import sys
from datetime import datetime

project_path = '/home/nikolark/dev/edb/mbftns/'
if project_path not in sys.path:
    sys.path.append(project_path)

from django.core.management import setup_environ
from django.core.mail import mail_admins
import settings

setup_environ(settings)

from main.models import *
from radius.models import *
logs = TempUserLog.objects.filter(expires__lt=datetime.now(), deleted=False)

for log in logs:
    for up in log.userpass_set.all():
        Radcheck.objects.filter(username=up.username).delete()
    log.deleted = True
    log.save()
