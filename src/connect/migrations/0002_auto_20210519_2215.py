# Generated by Django 2.1.5 on 2021-05-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicprofile',
            name='destination',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='publicprofile',
            name='origin',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
