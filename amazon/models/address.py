from django.db import models
from amazon.constants.enums import AddressType

Address_Type = (
    (AddressType.house.value, AddressType.house.value),
    (AddressType.apartment.value, AddressType.apartment.value),
    (AddressType.business.value, AddressType.business.value),
    (AddressType.other.value, AddressType.other.value)
)

class Address(models.Model):

    door_no = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255, choices=Address_Type)