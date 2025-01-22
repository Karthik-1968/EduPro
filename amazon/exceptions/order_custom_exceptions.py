class OrderDoesNotExistException(Exception):
    def __init__(self, order_id:int):
        self.order_id = order_id

    def __str__(self):
        return f"{self.order_id} does not exist"

class DeliveryAvailabilityAlreadyExistsException(Exception):
    pass

class DeliveryAvailabilityDoesNotExistException(Exception):
    def __init__(self, delivery_availability_id:int):
        self.delivery_availability_id = delivery_availability_id

    def __str__(self):
        return f"{self.delivery_availability_id} does not exist"

class DeliveryServiceAlreadyExistsException(Exception):
    pass

class DeliveryServiceDoesNotExistException(Exception):
    def __init__(self, delivery_service_id:int):
        self.delivery_service_id = delivery_service_id

    def __str__(self):
        return f"{self.delivery_service_id} does not exist"

class ItemDoesNotBelongToOrderException(Exception):
    def __init__(self, item_id:int, order_id:int):
        self.item_id = item_id
        self.order_id = order_id

    def __str__(self):
        return f"{self.item_id} does not belong to {self.order_id}"