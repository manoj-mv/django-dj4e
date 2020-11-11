# Generated by Django 3.1.1 on 2020-11-10 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos_dj4e', '0002_auto_20201109_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'minimum 5 characters required.')], verbose_name='Name(Auto)'),
        ),
    ]
