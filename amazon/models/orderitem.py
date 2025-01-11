from django.db import models
from .order import Order
from .item import Item
from .itememi import ItemEmi
from .itemoffer import ItemOffer
from .itemwarranty import ItemWarranty
from .itemexchangeproperty import ItemExchangeProperty
from .itemproperty import ItemProperty

class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_in_cart = models.BooleanField(default=False)
    itemproperties = models.ManyToManyField(ItemProperty, related_name="orderitem")
    itememi = models.ForeignKey(ItemEmi, on_delete=models.CASCADE, related_name="orderitem", null=True, blank=True)
    itemoffers = models.ManyToManyField(ItemOffer, related_name="orderitem", null=True, blank=True)
    itemwarranty = models.ForeignKey(ItemWarranty, on_delete=models.CASCADE, related_name="orderitem", null=True, blank=True)
    itemexchangeproperties = models.ManyToManyField(ItemExchangeProperty, related_name="orderitem", null=True, blank=True)