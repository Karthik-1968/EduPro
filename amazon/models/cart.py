from django.db import models

class Cart(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)