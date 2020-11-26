# Generated by Django 3.1.1 on 2020-11-26 05:20

from django.db import migrations, models
import pics_dj4e.models


class Migration(migrations.Migration):

    dependencies = [
        ('pics_dj4e', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='img',
            field=models.ImageField(upload_to=pics_dj4e.models.user_directory_path, validators=[pics_dj4e.models.file_size], verbose_name='Image'),
        ),
    ]
