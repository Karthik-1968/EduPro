from django.db import models
import uuid
from .address import Address

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=10, unique=True)