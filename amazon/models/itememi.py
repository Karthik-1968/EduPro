from django.db import models
from .item import Item
from .emi import Emi

class ItemEmi(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itememi")
    emi = models.ForeignKey(Emi, on_delete=models.CASCADE, related_name="itememi")