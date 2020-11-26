from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
# Create your models here.
from .custom_validators import file_size



# method to create path name fjipoorimage field
def user_directory_path(instance, filename):
    print('xxxxxx')
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'images/{0}/{1}'.format(instance.owner, filename)

class pic(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2,'Name field must have atleast 2 characters')],
        verbose_name='Name'
    )
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    img = models.ImageField(
        verbose_name='Image',
        upload_to=user_directory_path,
        validators = [file_size]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    