from django.db import models
from django.contrib.auth.models import User

class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)