from django.db import models

class DeliveryService(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)