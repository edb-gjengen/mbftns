from django.db import models
from django.contrib.auth.models import User

class TempUserLog(models.Model):
    who = models.CharField(max_length=255)
    why = models.CharField(max_length=255)
    expires = models.DateTimeField()
    issued_by = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    # TODO username and pass
