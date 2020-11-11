from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Make(models.Model):
    name = models.CharField(
            verbose_name='Name(Auto):',
            max_length=200,
            help_text='(eg.Honda)',
            validators=[MinLengthValidator(2,'minimum 2 characters required.')]
    )

    def __str__(self):
        return self.name

class Auto(models.Model):
    name = models.CharField(
            max_length=200,
            validators= [MinLengthValidator(5,'minimum 5 characters required.')],
            verbose_name='Name(Auto)'
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(
            'Make',
            on_delete=models.CASCADE,
            null=False
    )

    def __str__(self):
        return self.name