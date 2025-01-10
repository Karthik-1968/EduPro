from django.db import models

class DeliveryAvailability(models.Model):

    can_receive_on_saturday = models.BooleanField()
    can_receive_on_sunday = models.BooleanField()