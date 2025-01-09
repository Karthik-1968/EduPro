from django.db import models

class Property(models.Model):

    property_name = models.CharField(max_length=50, unique=True)