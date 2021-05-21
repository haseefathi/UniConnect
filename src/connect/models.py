from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class PublicProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    profile_public = models.BooleanField(default = False)

    origin_city = models.CharField(max_length = 100, blank = True, null=True)
    origin_country = CountryField(blank = True, blank_label = 'Select Country')
    destination_city = models.CharField(max_length = 100, blank = True, null=True)
    destination_country = CountryField(blank = True, blank_label = 'Select Country')
    
    accepted_university = models.CharField(max_length = 200, blank = True, null=True)
    major = models.CharField(max_length = 200, blank = True, null=True)
    
    date_of_birth = models.DateField(blank = True, null = True)
    profile = models.TextField(blank = True)

    profile_updated = models.BooleanField(default = False)

    