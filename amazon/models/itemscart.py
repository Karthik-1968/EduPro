from django.db import models
from .item import Item
from .cart import Cart
from .itemproperty import ItemProperty
from .itemwarranty import ItemWarranty
from .itemexchangeproperty import ItemExchangeProperty
from .itememi import ItemEmi
from .itemoffer import ItemOffer

class ItemsCart(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemscart")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="itemscart")
    itemwarranty = models.ForeignKey(ItemWarranty, on_delete=models.CASCADE, related_name="itemscart", null=True, blank=True)
    itemexchangeproperties = models.ManyToManyField(ItemExchangeProperty, related_name="itemscart", null=True, blank=True)
    itemproperties = models.ManyToManyField(ItemProperty, related_name="itemscart")