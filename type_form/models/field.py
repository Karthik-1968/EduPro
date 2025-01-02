from django.db import models


class Field(models.Model):
    
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)
    