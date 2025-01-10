from django.db import models
from .category import Category

class Item(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    number_of_left_in_stock = models.IntegerField()
    number_of_purchases_in_last_month = models.IntegerField()
    views = models.IntegerField(default=0)
