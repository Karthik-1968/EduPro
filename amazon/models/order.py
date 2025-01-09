from django.db import models
from .user import User
from .address import Address
from .item import Item
from .itemproperty import ItemProperty

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    itemproperties = models.ManyToManyField(ItemProperty, related_name="orders")
