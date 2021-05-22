from django import forms 
from django.contrib.auth.models import User
from .models import PublicProfile
from django_countries.fields import CountryField

from datetime import datetime, timedelta

STARTING_SEMESTER_CHOICES = (
    ('F', 'Fall'),
    ('S', 'Spring')
)

DEGREE_CHOICES = (
    ('ms', 'MS'),
    ('phd', 'PhD')
)

def is_number_present(string):
    return any(i.isdigit() for i in string)


class UpdatePublicProfileForm(forms.Form):
    profile = forms.CharField(widget = forms.Textarea, label = "Profile (Max. 500 characters)")
    date_of_birth = forms.DateField(label = "Date of Birth", widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    origin_city = forms.CharField(label = "Current City")
    origin_country = CountryField(blank_label = "Current Country").formfield()
    destination_city = forms.CharField(label = "Destination City")
    destination_country = CountryField(blank_label = "Select Destination Country").formfield()
    
    accepted_university = forms.CharField(label = "Accepted University Name")
    major = forms.CharField(label = "Major")

    starting_semester = forms.ChoiceField(choices = STARTING_SEMESTER_CHOICES, label = "Starting Semester")
    starting_year = forms.IntegerField(label = "Starting Year")
    degree = forms.ChoiceField(choices = DEGREE_CHOICES)

    

    # form validation functions
    # def clean_date_of_birth(self):
    #     cleaned_data = super(UpdatePublicProfileForm, self).clean()
    #     dob = cleaned_data.get("date_of_birth")
    #     print(dob)
    #     ten_years_prior = datetime.now() - timedelta(days=10*365)
    #     if  (dob >= ten_years_prior):
    #         raise forms.ValidationError(
    #             "Please enter a valid date of birth!"
    #         )
    #     return dob

    
    def clean_origin_city(self):
        cleaned_data = super(UpdatePublicProfileForm, self).clean()
        city = cleaned_data.get("origin_city")
        if (is_number_present(city)):
            raise forms.ValidationError(
                "Name of city cannot contain a number!"
            )
        return city
    

    def clean_destination_city(self):
        cleaned_data = super(UpdatePublicProfileForm, self).clean()
        city = cleaned_data.get("destination_city")
        if (is_number_present(city)):
            raise forms.ValidationError(
                "Name of city cannot contain a number!"
            )
        return city



    

    



