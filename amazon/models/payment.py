from django.db import models
from .order import Order
from .paymentmethod import PaymentMethod

class Payment(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name="payments")
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50, unique=True)
    gift_card_or_promo_code = models.CharField(max_length=50, null=True, blank=True)