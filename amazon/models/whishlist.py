from django.db import models

class Whishlist(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    items = models.ManyToManyField('Item', related_name="whishlists")