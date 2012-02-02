from django.db import models
from django.contrib.auth.models import User

class TempUserLog(models.Model):
    issued_by = models.ForeignKey(User)
    description = models.TextField(max_length=255)
    expires = models.DateTimeField()
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

class UserPass(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    radcheck_id = models.PositiveIntegerField(unique=True, null=False)
    log = models.ForeignKey(TempUserLog)
    
