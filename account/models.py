from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(unique=True, max_length=50, verbose_name='Е-мэйл')
    profile_image = models.ImageField(upload_to='users/', default='default.png', verbose_name="Аватарка")
    email = models.EmailField(unique=True, max_length=50, verbose_name='Е-мэйл')

    def save(self, *args, **kwargs):
        self.email = self.username
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
