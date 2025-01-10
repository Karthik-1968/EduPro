from django.db import models

class Warranty(models.Model):
    
    warranty_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    number_fo_years = models.IntegerField()
    total_amount = models.FloatField
    warranty_description = models.TextField()