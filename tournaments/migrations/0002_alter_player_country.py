# Generated by Django 5.0.7 on 2024-07-20 13:02

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
