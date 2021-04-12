from django import forms 
from django.contrib.auth.models import User
from .models import SiteUser


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class SignUpForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print(password, confirm_password)
        if password != confirm_password:
            raise forms.ValidationError(
                "The passwords do not match!"
            )
        return password

    def clean_email(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = cleaned_data.get("email")
        duplicate_users = User.objects.filter(email = email)
        if duplicate_users.exists():
            raise forms.ValidationError("E-mail is already registered!")
        return email
    
    def clean_username(self):
        cleaned_data = super(SignUpForm, self).clean()
        username = cleaned_data.get("username")
        duplicate_users = User.objects.filter(username = username)
        if duplicate_users.exists():
            raise forms.ValidationError("Username is already in use!")
        return username