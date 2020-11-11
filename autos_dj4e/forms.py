from django.forms import ModelForm
from autos_dj4e.models import Make

# class makeForm(ModelForm):
#     class Meta:
#         model = Make
#         fields = '__all__'
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'