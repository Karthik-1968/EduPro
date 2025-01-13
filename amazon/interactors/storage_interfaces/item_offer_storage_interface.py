from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import OfferDTO

class ItemOfferStorageInterface:

    @abstractmethod
    def check_if_offer_already_exists(self, offer_dto:OfferDTO):
        pass

    @abstractmethod
    def create_bank_offer(self, offer_dto:OfferDTO)->int:
        pass

    @abstractmethod
    def create_no_cost_emi_offer(self, offer_type:str)->int:
        pass

    @abstractmethod
    def create_coupon_offer(self, offer_dto:OfferDTO)->int:
        pass

    @abstractmethod
    def create_payment_offer(self, offer_dto:OfferDTO)->int:
        pass

    @abstractmethod
    def check_if_exchange_property_already_exists(self, property_name:str, property_value:str):
        pass

    @abstractmethod
    def create_exchange_property(self, property_name:str, property_value:str)->int:
        pass

    @abstractmethod
    def check_if_exchange_property_exists(self, exchange_property_id:int):
        pass

    @abstractmethod
    def check_if_exchange_value_already_exists(self, exchange_discount:float, service_charge:float):
        pass

    @abstractmethod
    def create_exchange_value(self, exchange_discount:float, service_charge:float)->int:
        pass

    @abstractmethod
    def check_if_exchange_value_exists(self, exchange_value_id:int):
        pass

    @abstractmethod
    def check_if_exchange_properties_exists(self, exchange_property_ids:list[int]):
        pass

    @abstractmethod
    def add_exchange_properties_to_exchange_value(self, exchange_value_id:int, exchange_property_ids:list[int]):
        pass

    @abstractmethod
    def add_exchange_properties_to_item(self, item_id:int, exchange_property_id:int):
        pass

    @abstractmethod
    def check_if_offer_exists(self, offer_id:int):
        pass

    @abstractmethod
    def add_offer_to_item(self, item_id:int, offer_id:int):
        pass

    @abstractmethod
    def add_offer_to_order(self, order_id:int, offer_id:int):
        pass

    @abstractmethod
    def add_exchange_properties_to_order(self, order_id:int, exchange_property_ids:list[int]):
        pass

    @abstractmethod
    def check_if_item_exchange_properties_exists(self, item_exchange_properties:list[int]):
        pass

    @abstractmethod
    def add_item_exchange_properties_to_order(self, order_id:int, item_exchange_properties:list[int]):
        pass

    @abstractmethod
    def check_if_offer_is_specific_to_item_in_order(self, order_id:int, offer_id:int):
        pass

    @abstractmethod
    def check_if_offer_is_already_added_to_order(self, order_id:int, offer_id:int):
        pass

    @abstractmethod
    def check_if_exchange_properties_are_associated_with_item_in_order(self, order_id:int, exchange_property_ids:list[int]):
        pass

    @abstractmethod
    def check_if_exchange_properties_are_already_added_to_order(self, order_id:int, exchange_property_ids:list[int]):
        pass

    @abstractmethod
    def add_exchange_properties_to_order(self, order_id:int, exchange_property_ids:list[int]):
        pass