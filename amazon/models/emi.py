from django.db import models

class Emi(models.Model):

    emi_type  = models.CharField(max_length=255, null=False, blank=False)
    emi_amount = models.FloatField()
    card_name = models.CharField(max_length=255, null=True, blank=True)
    processing_fee = models.FloatField(null=True, blank=True)
    minimum_purchase_value = models.FloatField(null=True, blank=True)
    number_of_months = models.IntegerField()
    intereset_in_rupees = models.FloatField()
    interest_in_percentage = models.FloatField()
    discount_in_rupees = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField()