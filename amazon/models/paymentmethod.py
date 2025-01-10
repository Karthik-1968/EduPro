from django.db import models

class PaymentMethod(models.Model):

    payment_type = models.CharField(max_length=50)
    card_type = models.CharField(max_length=50, null=True, blank=True)
    card_number = models.CharField(max_length=50, null=True, blank=True)
    card_holder_name = models.CharField(max_length=50, null=True, blank=True)
    expiry_date = models.CharField(max_length=20,null=True, blank=True)
    cvv = models.CharField(max_length=10, null=True, blank=True)
    card_type = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    upi_id = models.CharField(max_length=50, null=True, blank=True)

