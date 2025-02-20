from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='avatars')
    about = models.TextField(default='', blank=True)

    def __str__(self):
        return self.user.username