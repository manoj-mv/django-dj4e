from django.db import models
from django.core.validators import MinLengthValidator

from django.conf import settings
# Create your models here.


class Forum(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5,'Title must be greater than 5 characters')]
    )
    text = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='forum_owner'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    comments = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Comment',
        related_name='forum_comments'
    )
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(
        validators=[MinLengthValidator(5,'comment must be greater than 5 charecters')]
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    

    