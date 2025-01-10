from django.db import models
from .item import Item
from .user import User
from amazon.constants.enums import RatingChoices

Rating_Choices = (
    (RatingChoices.one.value, RatingChoices.one.value),
    (RatingChoices.two.value, RatingChoices.two.value),
    (RatingChoices.three.value, RatingChoices.three.value),
    (RatingChoices.four.value, RatingChoices.four.value),
    (RatingChoices.five.value, RatingChoices.five.value),
)

class Rating(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    rating = models.CharField(max_length=50, choices=Rating_Choices)