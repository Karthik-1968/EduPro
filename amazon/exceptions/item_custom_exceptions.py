class ItemAlreadyExistsException(Exception):
    pass

class ItemDoesNotExistException(Exception):
    def __init__(self, item_id:int):
        self.item_id = item_id

    def __str__(self):
        return f"{self.item_id} does not exist"

class PropertyAlreadyExistsException(Exception):
    pass

class PropertyDoesNotExistException(Exception):
    def __init__(self, property_id:int):
        self.property_id = property_id

    def __str__(self):
        return f"{self.property_id} does not exist"

class ItemPropertyDoesNotExistException(Exception):
    def __init__(self, item_property_id:int):
        self.item_property_id = item_property_id

    def __str__(self):
        return f"{self.item_property_id} does not exist"

class OutOfStockException(Exception):
    pass

class CartAlreadyCreatedException(Exception):
    pass

class CartDoesNotExistException(Exception):
    def __init__(self, cart_id:int):
        self.cart_id = cart_id

    def __str__(self):
        return f"{self.cart_id} does not exist"

class ItemIsNotRatedException(Exception):
    def __init__(self, item_id:int):
        self.item_id = item_id

    def __str__(self):
        return f"{self.item_id} is not rated"

class EmiAlreadyExistsException(Exception):
    pass

class EmiDoesNotExistException(Exception):
    def __init__(self, emi_id:int):
        self.emi_id = emi_id

    def __str__(self):
        return f"{self.emi_id} does not exist"

class WarrantyAlreadyExistsException(Exception):
    pass

class WarrantyDoesNotExistException(Exception):
    def __init__(self, warranty_id:int):
        self.warranty_id = warranty

    def __str__(self):
        return f"{self.warranty_id} does not exist"

class OfferAlreadyExistsException(Exception):
    pass

class ExchangePropertyAlreadyExistsException(Exception):
    pass

class ExchangeValueAlreadyExistsException(Exception):
    pass

class ExchangeValueDoesNotExistException(Exception):
    def __init__(self, exchange_value_id:int):
        self.exchange_value_id = exchange_value_id

    def __str__(self):
        return f"{self.exchange_value_id} does not exist"

class ExchangePropertyDoesNotExistException(Exception):
    def __init__(self, exchange_property_id:int):
        self.exchange_property_id = exchangeproperty_id

    def __str__(self):
        return f"{self.exchange_property_id} does not exist"

class OfferDoesNotExistException(Exception):
    def __init__(self, offer_id:int):
        self.offer_id = offer_id

    def __str__(self):
        return f"{self.offer_id} does not exist"

class ItemExchangePropertyDoesNotExistException(Exception):
    def __init__(self, itemexchange_property_id:int):
        self.itemexchange_property_id = itemexchange_property_id

    def __str__(self):
        return f"{self.itemexchange_property_id} does not exist"

class ItemWarrantyDoesNotExistException(Exception):
    def __init__(self, itemwarranty_id:int):
        self.itemwarranty_id = itemwarranty_id

    def __str__(self):
        return f"{self.itemwarranty_id} does not exist"

class ItemDoesNotExistInCartException(Exception):
    def __init__(self, item_id:int, cart_id:int):
        self.item_id = item_id
        self.cart_id = cart_id

    def __str__(self):
        return f"{self.item_id} does not exist in {self.cart_id}"

class WhishlistAlreadyCreatedException(Exception):
    pass

class WhishlistDoesNotExistException(Exception):
    def __init__(self, whishlist_id:int):
        self.whishlist_id = whishlist_id

    def __str__(self):
        return f"{self.whishlist_id} does not exist"

class ItemDoesNotExistInWhishlistException(Exception):
    def __init__(self, item_id:int, whishlist_id:int):
        self.item_id = item_id
        self.whishlist_id = whishlist_id

    def __str__(self):
        return f"{self.item_id} does not exist in {self.whishlist_id}"

class PropertyAlreadyAddedToItemException(Exception):
    def __init__(self, property_id:int, item_id:int):
        self.property_id = property_id
        self.item_id = item_id

    def __str__(self):
        return f"{self.property_id} already added to {self.item_id}"

class UserHasNotViewedAnyItemException(Exception):
    def __init__(self, user_id:str):
        self.user_id = user_id

    def __str__(self):
        return f"{self.user_id} has not viewed any item"

class UserAlreadyRatedItemException(Exception):
    def __init__(self, user_id:str, item_id:int):
        self.user_id = user_id
        self.item_id = item_id

    def __str__(self):
        return f"{self.user_id} already rated {self.item_id}"

class ItemEmiDoesNotExistException(Exception):
    def __init__(self, item_emi_id:int):
        self.item_emi_id = item_emi_id

    def __str__(self):
        return f"{self.item_emi_id} does not exist"

class ItemEmiIsNotAssociatedWithItemException(Exception):
    def __init__(self, item_emi_id:int, item_id:int):
        self.item_emi_id = item_emi_id
        self.item_id = item_id

    def __str__(self):
        return f"{self.item_emi_id} is not associated with {self.item_id}"

class ItemEmiAlreadyAddedToOrderException(Exception):
    def __init__(self, item_emi_id:int, order_id:int):
        self.item_emi_id = item_emi_id
        self.order_id = order_id

    def __str__(self):
        return f"{self.item_emi_id} already added to {self.order_id}"

class ItemOfferIsNotSpecificToItemException(Exception):
    def __init__(self, item_offer_id:int, item_id:int):
        self.item_offer_id = item_offer_id
        self.item_id = item_id

    def __str__(self):
        return f"{self.item_offer_id} is not specific to {self.item_id}"

class ItemOfferAlreadyAddedToOrderException(Exception):
    def __init__(self, item_offer_id:int, order_id:int):
        self.item_offer_id = item_offer_id
        self.order_id = order_id

    def __str__(self):
        return f"{self.item_offer_id} already added to {self.order_id}"

class ExchangePropertiesAreNotAssociatedWithItemInOrderException(Exception):
    pass

class ExchangePropertiesAreAlreadyAddedToOrderException(Exception):
    pass

class ItemPropertyDoesNotBelongToItemException(Exception):
    def __init__(self, item_property_id:int, item_id:int):
        self.item_property_id = item_property_id
        self.item_id = item_id

    def __str__(self):
        return f"{self.item_property_id} does not belong to {self.item_id}"

class ItemWarrantyIsNotAssociatedWithItemException(Exception):
    def __init__(self, warranty_id:int, item_id:int):
        self.warranty_id = warranty

    def __str__(self):
        return f"{self.warranty_id} is not associated with {self.item_id}"

class ItemWarrantyAlreadyAssociatedWithOrderException(Exception):
    def __init__(self, warranty_id:int, order_id:int):
        self.warranty_id = warranty_id
        self.order_id = order_id

    def __str__(self):
        return f"{self.warranty_id} already associated with {self.order_id}"