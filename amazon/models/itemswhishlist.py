from django.db import models
from .item import Item
from .itemproperty import ItemProperty
from .whishlist import Whishlist

class ItemsWhishlist(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemswhishlist")
    whishlist = models.ForeignKey(Whishlist, on_delete=models.CASCADE, related_name="itemswhishlist")
    itemproperties = models.ManyToManyField(ItemProperty, related_name="itemswhishlist")