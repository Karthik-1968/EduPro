from django.db import models

class ExchangeProperty(models.Model):
    
    exchange_property_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    exchange_property_value = models.CharField(max_length=255, unique=True, null=False, blank=False)