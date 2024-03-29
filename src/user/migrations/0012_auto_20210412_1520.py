# Generated by Django 2.1 on 2021-04-12 11:20

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_siteuser_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='gre_awa_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.0), user.models.awa_score_validator]),
        ),
    ]
