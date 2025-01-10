class UserAlreadyExistsException(Exception):
    pass

class AddressAlreadyExistsException(Exception):
    pass

class UserDoesNotExistException(Exception):
    pass

class AddressDoesNotExistException(Exception):
    pass

class AddressAlreadyAddedToUserException(Exception):
    pass

class CategoryAlreadyExistsException(Exception):
    pass

class ItemAlreadyExistsException(Exception):
    pass

class CategoryDoesNotExistException(Exception):
    pass

class ItemDoesNotExistException(Exception):
    pass

class PropertyAlreadyExistsException(Exception):
    pass

class PropertyDoesNotExistException(Exception):
    pass

class PropertyAlreadyAddedToItemException(Exception):
    pass

class PaymentMethodAlreadyExistsException(Exception):
    pass

class PaymentMethodDoesNotExistException(Exception):
    pass

class OrderDoesNotExistException(Exception):
    pass

class ItemPropertyDoesNotExistException(Exception):
    pass

class UserAddressDoesNotExistException(Exception):
    pass

class OutOfStockException(Exception):
    pass

class CartAlreadyCreatedException(Exception):
    pass

class CartDoesNotExistException(Exception):
    pass

class ItemIsNotRatedException(Exception):
    pass

class EmiAlreadyExistsException(Exception):
    pass

class EmiDoesNotExistException(Exception):
    pass

class WarrantyAlreadyExistsException(Exception):
    pass

class WarrantyDoesNotExistException(Exception):
    pass

class DeliveryAvailabilityAlreadyExistsException(Exception):
    pass

class DeliveryAvailabilityDoesNotExistException(Exception):
    pass

class OfferAlreadyExistsException(Exception):
    pass

class ExchangePropertyAlreadyExistsException(Exception):
    pass

class ExchangeValueAlreadyExistsException(Exception):
    pass

class ExchangeValueDoesNotExistException(Exception):
    pass

class ExchangePropertyDoesNotExistException(Exception):
    pass

class OfferDoesNotExistException(Exception):
    pass

class ItemExchangePropertyDoesNotExistException(Exception):
    pass

class ItemWarrantyDoesNotExistException(Exception):
    pass

class ItemDoesNotExistInCartException(Exception):
    pass

class WhishlistAlreadyCreatedException(Exception):
    pass

class WhishlistDoesNotExistException(Exception):
    pass

class ItemDoesNotExistInWhishlistException(Exception):
    pass

class UserHasNotViewedAnyItemException(Exception): 
    pass

class UserAlreadyRatedItemException(Exception):
    pass