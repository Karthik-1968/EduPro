from django.db import models
from .exchangeproperty import ExchangeProperty

class ExchangeValue(models.Model):

    exchange_value = models.FloatField()
    exchange_service_fee = models.FloatField()
    exchangeproperties = models.ManyToManyField(ExchangeProperty, related_name="exchangevalues")