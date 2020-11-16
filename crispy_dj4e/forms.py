from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class demo_form(forms.Form):
    title =forms.CharField(
        label='Name :',
        validators=[
            validators.MinLengthValidator(2,'Atleast 2 char rquired.')
        ]
    )
    mileage=forms.IntegerField()
    p_date=forms.DateField()

