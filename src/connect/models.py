from django.db import models
from django.contrib.auth.models import User


class PublicProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    origin = models.CharField(max_length = 150, blank = True)
    destination = models.CharField(max_length = 150, blank = True)
    profile_public = models.BooleanField(default = False)
    