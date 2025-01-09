from django.db import models
from .item import Item

class Cart(models.Model):

    user = models.OneToOneField('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, related_name="carts")