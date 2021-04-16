from django import forms 
from django.contrib.auth.models import User
from .models import SiteUser


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

DEGREE_CHOICES = (
    ('ms', 'MS'),
    ('phd', 'PhD')
)

INTENDED_SEMESTER_CHOICES = (
    ('F', 'Fall'),
    ('S', 'Spring')
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


class UpdateProfileForm(forms.Form):
    degree = forms.ChoiceField(choices = DEGREE_CHOICES)
    gre_verbal_score = forms.IntegerField()
    gre_quant_score = forms.IntegerField()
    gre_awa_score = forms.DecimalField()
    toefl_score = forms.IntegerField()
    intended_semester = forms.ChoiceField(choices = INTENDED_SEMESTER_CHOICES)
    undergraduate_gpa = forms.DecimalField()

    def clean_gre_verbal_score(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        verbal_score = cleaned_data.get("gre_verbal_score")
        if not (verbal_score >= 130 and verbal_score <=170):
            raise forms.ValidationError(
                "Please enter a valid score! The score should be between 130 and 170."
            )
        return verbal_score

    def clean_gre_quant_score(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        quant_score = cleaned_data.get("gre_quant_score")
        if not (quant_score >= 130 and quant_score <=170):
            raise forms.ValidationError(
                "Please enter a valid score! The score should be between 130 and 170."
            )
        return quant_score

    def clean_gre_awa_score(self):
        valid_scores = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
        cleaned_data = super(UpdateProfileForm, self).clean()
        awa_score = cleaned_data.get("gre_awa_score")
        if awa_score not in valid_scores:
            raise forms.ValidationError(
                "Please enter a valid score!"
            )
        return awa_score

    def clean_toefl_score(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        toefl = cleaned_data.get("toefl_score")
        if not (toefl >= 0 and toefl <=120):
            raise forms.ValidationError(
                "Please enter a valid score! The score should be between 0 and 120."
            )
        return toefl

    def clean_undergraduate_gpa(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        gpa = cleaned_data.get('undergraduate_gpa')
        if not (gpa >= 0 and gpa <=4):
            raise forms.ValidationError(
                "Please enter a valid GPA between 0.0 and 4.0."
            )
        return gpa
