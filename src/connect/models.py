from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django_countries.fields import CountryField

DEGREE_CHOICES = (
    ('ms', 'MS'),
    ('phd', 'PhD')
)

STARTING_SEMESTER_CHOICES = (
    ('F', 'Fall'),
    ('S', 'Spring')
)


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

    degree = models.CharField(choices = DEGREE_CHOICES, default = 'ms', max_length = 3)
    starting_semester = models.CharField(choices = STARTING_SEMESTER_CHOICES, max_length = 5, blank = True, null=True, default = 'F')

    starting_year = models.IntegerField(blank = True, null = True)


class Friend_Request(models.Model):
    from_user = models.ForeignKey(
        User, related_name='from_user', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name='to_user', on_delete=models.CASCADE
    )

class Friendships(models.Model):
    subject = models.ForeignKey(
        User, related_name='subject', on_delete=models.CASCADE
    )
    friend = models.ForeignKey(
        User, related_name='friend', on_delete=models.CASCADE
    )


    