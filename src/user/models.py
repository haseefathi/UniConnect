from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# for field validations
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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

def awa_score_validator(value):
    valid_scores = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
    if value not in valid_scores:
        raise ValidationError(
            _('%(value)s is not a valid score'),
            params={'value': value},
        )


# Create your models here.
class GraduateAdmissionsProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    degree = models.CharField(choices = DEGREE_CHOICES, default = 'ms', max_length = 3)
    gre_verbal_score = models.IntegerField(validators = [MinValueValidator(130), MaxValueValidator(170)], blank = True, null=True)
    gre_quant_score = models.IntegerField(validators = [MinValueValidator(130), MaxValueValidator(170)], blank = True, null=True)
    gre_awa_score = models.DecimalField(max_digits = 2, decimal_places = 1,  validators = [MinValueValidator(0.0), MaxValueValidator(6.0), awa_score_validator], blank = True, null=True)
    intended_semester = models.CharField(choices = INTENDED_SEMESTER_CHOICES, max_length = 5, blank = True, null=True, default = 'F')
    toefl_score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(120)], blank = True, null=True)
    undergrad_gpa = models.DecimalField( max_digits = 2, decimal_places = 1,  validators = [MinValueValidator(0.0), MaxValueValidator(6.0)], blank = True, null=True)
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 6, default = 'F')
    intended_field = models.CharField(max_length = 50, blank = True, null=True)
    is_profile_updated = models.BooleanField(default = False)




class UniversityRecommendation(models.Model):
    user = models.ForeignKey(User, related_name='user_recommendation', on_delete=models.CASCADE)
    recommendation = models.CharField(max_length = 200, blank = True)
    image_url = models.URLField(max_length = 255, blank = True)
    recommendation_type = models.IntegerField(blank = True, null = True)