from django.db import models
from .item import Item

class Rating(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="ratings")
    five_stars_rating = models.IntegerField(default=0)
    four_stars_rating = models.IntegerField(default=0)
    three_stars_rating = models.IntegerField(default=0)
    two_stars_rating = models.IntegerField(default=0)
    one_star_rating = models.IntegerField(default=0)