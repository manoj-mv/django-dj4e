from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings



# Create your models here.


class Thing(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2,"Title must be greater than two characters.")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    favourite = models.ManyToManyField(
        settings.AUTH_USER_MODEL , through='Fav',related_name='favourite_things'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Fav(models.Model):
    thing = models.ForeignKey(Thing,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='favs_user')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['thing','user'],name='unique_favourite')
        ]
    def __str__(self):
        return '{0} likes {1}'.format(self.user.username,self.thing.title[:10])
    
