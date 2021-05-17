from django.db import models
from django.contrib.auth.models import User


DEGREE_CHOICES = (
    ('ms', 'MS'),
    ('phd', 'PhD')
)

INTENDED_SEMESTER_CHOICES = (
    ('F', 'Fall'),
    ('S', 'Spring')
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


# Create your models here.
class PublicProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    degree = models.CharField(choices = DEGREE_CHOICES, default = 'ms', max_length = 3)
    semester = models.CharField(choices = INTENDED_SEMESTER_CHOICES, max_length = 5, blank = True, null=True, default = 'F')
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 6, default = 'F')
    major = models.CharField(max_length = 50, blank = True, null=True)
    university = models.CharField(max_length = 100, blank = True, null=True)
    origin = models.CharField(max_length = 100, blank = True, null = True)
    destination = models.CharField(max_length = 100, blank = True, null = True)