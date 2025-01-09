from django.db import models
from .item import Item
from .property import Property

class ItemProperty(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)