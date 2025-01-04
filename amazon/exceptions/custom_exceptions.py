class UserAlreadyExists(Exception):
    pass

class AddressAlreadyExists(Exception):
    pass

class UserDoesNotExist(Exception):
    pass

class AddressDoesNotExist(Exception):
    pass

class AddressAlreadyAddedToUser(Exception):
    pass

class CategoryAlreadyExists(Exception):
    pass

class ItemAlreadyExists(Exception):
    pass

class CategoryDoesNotExist(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class PropertyAlreadyExists(Exception):
    pass

class PropertyDoesNotExist(Exception):
    pass

class PropertyAlreadyAddedToItem(Exception):
    pass

class PaymentMethodAlreadyExists(Exception):
    pass

class PaymentMethodDoesNotExist(Exception):
    pass

class OrderDoesNotExist(Exception):
    pass