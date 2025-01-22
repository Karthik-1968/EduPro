from django.db import models
from .user import User
from .order import Order
from .item import Item

class Refund(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='refunds')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='refunds')
    amount = models.FloatField()
    refund_status = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    reason = models.TextField()
    refund_with_in_days = models.IntegerField(null=True, blank=True)
    items = models.ManyToManyField(Item, related_name='refunds', null=True, blank=True)