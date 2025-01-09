from django.db import models
from .item import Item
from .user import User

class ItemView(models.Model):
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="itemviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="itemviews")
    viewed_at = models.DateTimeField(auto_now=True)
    views= models.IntegerField(default=0)