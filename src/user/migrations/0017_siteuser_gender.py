# Generated by Django 2.1.5 on 2021-04-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_siteuser_is_profile_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='F', max_length=6),
        ),
    ]