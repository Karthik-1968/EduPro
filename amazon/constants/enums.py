from enum import Enum

class AddressType(Enum):
    
    house = "HOUSE"
    apartment = "APARTMENT"
    business = "BUSINESS"
    other = "OTHER"

class RatingChoices(Enum):
    
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"