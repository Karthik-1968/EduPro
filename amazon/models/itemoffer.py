from django.db import models
from .item import Item
from .offer import Offer

class ItemOffer(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemoffers")
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="itemoffers")