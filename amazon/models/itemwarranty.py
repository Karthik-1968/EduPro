from django.db import models
from .item import Item
from .warranty import Warranty

class ItemWarranty(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemwarranty")
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE, related_name="itemwarranty")