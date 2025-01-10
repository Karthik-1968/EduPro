from django.db import models
from .user import User
from .address import Address
from .item import Item
from .itemproperty import ItemProperty
from .itemwarranty import ItemWarranty
from .cart import Cart
from .delivery_availability import DeliveryAvailability
from .deliveryservice import DeliveryService


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    itemproperties = models.ManyToManyField(ItemProperty, related_name="orders", null=True, blank=True)
    delivery_charges = models.FloatField(null=True, blank=True)
    receiving_person_name = models.CharField(max_length=100, null=True, blank=True)
    delivered_by = models.ForeignKey(DeliveryService, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    itemwarranty = models.ForeignKey(ItemWarranty, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    delivery_availability = models.ForeignKey(DeliveryAvailability, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    
