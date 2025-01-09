from django.db import models
from .item import Item
from .cart import Cart
from .itemproperty import ItemProperty

class ItemsCart(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemscart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="itemscart")
    itemproperties = models.ManyToManyField(ItemProperty, related_name="itemscart")