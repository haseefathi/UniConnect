# Generated by Django 2.1 on 2021-04-12 11:22

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210412_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='gre_awa_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.0), user.models.awa_score_validator]),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='gre_quant_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(130), django.core.validators.MaxValueValidator(170)]),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='gre_verbal_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(130), django.core.validators.MaxValueValidator(170)]),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='intended_semester',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='toefl_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='undergrad_gpa',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.0)]),
        ),
    ]
