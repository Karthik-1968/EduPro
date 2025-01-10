from django.db import models

class Offer(models.Model):

    offer_type = models.CharField(max_length=255, null=False, blank=False)
    offer_name = models.CharField(max_length=255, null=True, blank=True)
    card_name = models.CharField(max_length=255, null=True, blank=True)
    discount_in_rupees = models.FloatField()
    discount_in_percentage = models.FloatField()
    minimum_purchase_value = models.FloatField(null=True, blank=True)
    minimum_months_emi = models.IntegerField(null=True, blank=True)
    coupoun_code = models.CharField(max_length=255, null=True, blank=True)
    minimum_number_of_items = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    terms_and_conditions = models.TextField()