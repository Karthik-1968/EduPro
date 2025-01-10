from django.db import models
from .item import Item
from .exchangeproperty import ExchangeProperty

class ItemExchangeProperty(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemexchangeproperty")
    exchangeproperty = models.ForeignKey(ExchangeProperty, on_delete=models.CASCADE, related_name="itemexchangeproperty")