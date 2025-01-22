from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import OrderIdDTO

class OrderPresenterInterface:

    @abstractmethod
    def get_response_for_create_order_for_item(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_get_orders_of_user(self, orderid_dtos:list[OrderIdDTO])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_get_orders_of_item(self, orderid_dtos:list[OrderIdDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_order_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_delete_order(self):
        pass

    @abstractmethod
    def get_response_for_create_order_for_cart(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_create_delivery_avalibility(self, delivery_avalibility_id:int):
        pass

    @abstractmethod
    def raise_exception_for_delivery_availability_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_delivery_availability_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_delivery_availability_already_exists():
        pass

    @abstractmethod
    def get_response_for_create_delivery_availability(self, delivery_availability_id:int):
        pass

    @abstractmethod
    def raise_exception_for_delivery_availability_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_delivery_service(self, delivery_service_id:int):
        pass

    @abstractmethod
    def raise_exception_for_delivery_service_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_delivery_service_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_belong_to_cart(self):
        pass

    @abstractmethod
    def raise_exception_for_delivery_service_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_belong_to_order(self):
        pass

    @abstractmethod
    def get_response_for_delete_particular_items_in_order(self):
        pass