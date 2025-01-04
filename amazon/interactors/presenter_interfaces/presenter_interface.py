from abc import abstractmethod
from amazon.interactors.storage_interfaces.storage_interface import CategoryDTO, ItemDTO, OrderDTO

class PresenterInterface:

    @abstractmethod
    def raise_exception_for_missing_user_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_user_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_email(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_contact_number(self):
        pass

    @abstractmethod
    def raise_exception_for_user_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_user(self, user_id:str):
        pass

    @abstractmethod
    def raise_exception_for_missing_street(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_city(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_district(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_state(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_country(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_pincode(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_contact_number(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_address_type(self):
        pass

    @abstractmethod
    def raise_exception_for_address_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_address(self, address_id:str):
        pass

    @abstractmethod
    def raise_exception_for_missing_address_id(self):
        pass

    @abstractmethod
    def raise_exception_for_user_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_address_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_address_already_added_to_user(self):
        pass

    @abstractmethod
    def get_response_for_add_address_to_user(self, useraddress_id:str):
        pass

    @abstractmethod
    def raise_exception_for_missing_category_name(self):
        pass

    @abstractmethod
    def raise_exception_for_category_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_category(self, category_id:int):
        pass

    @abstractmethod
    def get_response_for_list_of_categories(self, category_dtos:list[CategoryDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_missing_item_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_category_id(self):
        pass
    
    @abstractmethod
    def raise_exception_for_missing_price(self):
        pass
    
    @abstractmethod
    def raise_exception_for_item_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_item(self, item_id:int):
        pass

    @abstractmethod
    def get_response_for_list_of_items(self, item_dtos:list[ItemDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_category_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_list_of_items_by_category(self, item_dtos:list[ItemDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_missing_property_name(self):
        pass

    @abstractmethod
    def raise_exception_for_property_already_exists(self):
        pass
    
    @abstractmethod
    def get_response_for_create_property(self, property_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_item_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_property_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_value(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_property_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_property_already_added_to_item(self):
        pass

    @abstractmethod
    def get_response_for_add_property_to_item(self, itemproperty_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_status(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_delivery_date(self):
        pass

    @abstractmethod
    def get_response_for_create_order(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_get_orders_of_user(self, order_dtos:list[OrderDTO])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_get_orders_of_item(self, order_dtos:list[OrderDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_payment_method_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def raise_exception_for_paymentmethod_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_order_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_order_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_paymentmethod_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_payment_status(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_amount(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_transaction_id(self):
        pass

    @abstractmethod
    def get_response_for_add_payment_to_order(self, payment_id:int):
        pass

