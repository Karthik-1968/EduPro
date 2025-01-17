from django.db import models
from .user import User
from .address import Address
from .deliveryavailability import DeliveryAvailability
from .deliveryservice import DeliveryService

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    ordered_at = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    delivery_charges = models.FloatField(null=True, blank=True)
    receiving_person_name = models.CharField(max_length=100, null=True, blank=True)
    delivered_by = models.ForeignKey(DeliveryService, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    delivery_availability = models.ForeignKey(DeliveryAvailability, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)