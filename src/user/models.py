from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

score_size = models.IntegerField(validators = [MinValueValidator(130), MaxValueValidator(170)] )

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # degree = models.CharField()
    gre_verbal_score = models.IntegerField(default= 150, validators = [MinValueValidator(130), MaxValueValidator(170)], blank = True)
    gre_quant_score = models.IntegerField(default= 152, validators = [MinValueValidator(130), MaxValueValidator(170)], blank = True)
    gre_awa_score = models.DecimalField(default=3.5, max_digits = 2, decimal_places = 1,  validators = [MinValueValidator(0.0), MaxValueValidator(6.0)], blank = True)
    intended_semester = models.CharField(max_length = 5, default = 'F', blank = True)
    toefl_score = models.IntegerField(default= 152, validators = [MinValueValidator(130), MaxValueValidator(170)], blank = True)
    undergrad_gpa = models.DecimalField(default=3.0, max_digits = 2, decimal_places = 1,  validators = [MinValueValidator(0.0), MaxValueValidator(6.0)], blank = True)
