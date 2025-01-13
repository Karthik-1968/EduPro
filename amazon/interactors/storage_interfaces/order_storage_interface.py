from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import OrderItemDTO, OrderIdDTO, OrderCartItemsDTO

class OrderStorageInterface:

    @abstractmethod
    def create_order_for_item(self, order_dto:OrderItemDTO)->int:
        pass

    @abstractmethod
    def get_orders_of_user(self, user_id:str)->list[OrderIdDTO]:
        pass

    @abstractmethod
    def get_orders_of_item(self, item_id:int)->list[OrderIdDTO]:
        pass

    @abstractmethod
    def check_if_order_exists(self, order_id:int):
        pass

    @abstractmethod
    def delete_order(self, order_id:int):
        pass

    @abstractmethod
    def create_order_for_cart(self, order_dto:OrderCartItemsDTO)->int:
        pass

    @abstractmethod
    def add_emi_to_order(self, order_id:int, emi_id:int):
        pass

    @abstractmethod
    def create_delivery_availability(self, can_receive_on_saturday:bool, can_receive_on_sunday:bool)->int:
        pass

    @abstractmethod
    def check_if_delivery_availability_exists(self, delivery_availability_id:int):
        pass

    @abstractmethod
    def add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int):
        pass

    @abstractmethod
    def check_if_delivery_availability_already_exists(self, can_receive_on_saturday:bool, can_receive_on_sunday:bool):
        pass

    @abstractmethod
    def check_if_delivery_service_already_exists(self, name:str, email:str, contact_number:str):
        pass

    @abstractmethod
    def create_delivery_service(self, name:str, email:str, contact_number:str)->int:
        pass

    @abstractmethod
    def check_if_delivery_service_exists(self, delivery_service_id:int):
        pass

    @abstractmethod
    def add_delivery_service_to_order(self, order_id:int, delivery_service_id:int):
        pass