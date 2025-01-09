from django.db import models
from .user import User
from .address import Address

class UserAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)