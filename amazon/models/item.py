from django.db import models
from .category import Category


class Item(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    number_of_left_in_stock = models.IntegerField()
    number_of_purchases_in_last_month = models.IntegerField()
    views = models.IntegerField(default=0)
    discount_in_percentage = models.FloatField(null=True, blank=True)
    discount_in_rupees = models.FloatField(null=True, blank=True)
    service_replacement_in_days = models.IntegerField(null=True, blank=True)
    is_top_brand = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    is_new_release = models.BooleanField(default=False)
    payment = models.CharField(max_length=50, null=True, blank=True)
    ships_from = models.CharField(max_length=50, null=True, blank=True)
    sold_by = models.CharField(max_length=50, null=True, blank=True)
    packaging = models.CharField(max_length=50, null=True, blank=True)
    about_this_item = models.TextField(null=True, blank=True)


