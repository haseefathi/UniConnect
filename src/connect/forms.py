from django import forms 
from django.contrib.auth.models import User
from .models import PublicProfile
from django_countries.fields import CountryField

class UpdatePublicProfileForm(forms.Form):
    profile = forms.CharField(widget = forms.Textarea, label = "Profile")
    date_of_birth = forms.DateField(label = "Date of Birth")

    origin_city = forms.CharField(label = "Origin City")
    origin_country = CountryField(blank_label = "Select Origin Country").formfield()
    destination_city = forms.CharField(label = "Destination City")
    destination_country = CountryField(blank_label = "Select Destination Country").formfield()
    
    accepted_university = forms.CharField(label = "Accepted University")
    major = forms.CharField(label = "Major")
