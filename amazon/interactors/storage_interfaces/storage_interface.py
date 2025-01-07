from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class CategoryDTO:
    category_name:str

@dataclass
class ItemDTO:
    category_id:int
    item_name:str
    price:float
    number_of_left_in_stock:int
    views:int

@dataclass
class OrderDTO:
    user_id:str
    item_id:int
    address_id:int
    status:str
    delivery_date:str
    properties:list[int]

@dataclass
class PaymentMethodDTO:
    payment_type:str
    card_name:Optional[str]=None
    card_number:Optional[str]=None
    card_holder_name:Optional[str]=None
    cvv:Optional[str]=None
    expiry_date:Optional[str]=None
    bank_name:Optional[str]=None
    username:Optional[str]=None
    password:Optional[str]=None
    upi_id:Optional[str]=None

@dataclass
class OrderPaymentDTO:
    order_id:int
    paymentmethod_id:int
    status:str
    amount:int
    transaction_id:str
    gift_card_or_promo_code:str

@dataclass
class EmiDTO:
    emi_type:str
    processing_fee:Optional[float]
    minimum_purchase_value:Optional[float]
    discount:Optional[float]
    number_of_months:int
    interest_in_rupees:float
    interest_in_percentage:float
    total_amount:float
    card_name:Optional[str]=None
    debit_card_name:Optional[str]=None

class StorageInterface:

    @abstractmethod
    def check_if_user_already_exists(self, email:str, contact_number:str):
        pass

    @abstractmethod
    def create_user(self, id:str, name:str, email:str, contact_number:str)->str:
        pass

    @abstractmethod
    def check_if_address_already_exists(self, door_no:str, street:str, city:str, district:str, state:str, country:str, pincode:str):
        pass

    @abstractmethod
    def create_address(self, door_no:str, street:str, city:str, district:str, state:str, country:str, pincode:str,\
                                contact_number:str, address_type:str)->int:
        pass

    @abstractmethod
    def check_if_user_exists(self, user_id:str):
        pass

    @abstractmethod
    def check_if_address_exists(self, address_id:str):
        pass

    @abstractmethod
    def check_if_address_already_added_to_user(self, user_id:str, address_id:str):
        pass

    @abstractmethod
    def add_address_to_user(self, user_id:str, address_id:str)->int:
        pass

    @abstractmethod
    def check_if_category_already_exists(self, category_name:str):
        pass

    @abstractmethod
    def create_category(self, category_name:str)->int:
        pass

    @abstractmethod
    def get_list_of_categories(self)->list[CategoryDTO]:
        pass

    @abstractmethod
    def check_if_item_already_exists(self, item_name:str):
        pass

    @abstractmethod
    def create_item(self, item_name:str, category_id:int, price:float, number_of_left_in_stock:int)->int:
        pass

    @abstractmethod
    def get_list_of_items(self)->list[ItemDTO]:
        pass

    @abstractmethod
    def check_if_category_exists(self, category_id:int):
        pass

    @abstractmethod
    def get_list_of_items_by_category(self, category_id:int)->list[ItemDTO]:
        pass

    @abstractmethod
    def check_if_property_already_exists(self, property_name:str):
        pass

    @abstractmethod
    def create_property(self, property_name:str)->int:
        pass

    @abstractmethod
    def check_if_item_exists(self, item_id:int):
        pass

    @abstractmethod
    def check_if_property_exists(self, property_id:int):
        pass

    @abstractmethod
    def check_if_property_already_added_to_item(self, item_id:int, property_id:int, value:str):
        pass

    @abstractmethod
    def add_property_to_item(self, item_id:int, property_id:int, value:str)->int:
        pass

    @abstractmethod
    def create_order(self, order_dto:OrderDTO)->int:
        pass

    @abstractmethod
    def get_orders_of_user(self, user_id:str)->list[OrderDTO]:
        pass

    @abstractmethod
    def get_orders_of_item(self, item_id:int)->list[OrderDTO]:
        pass

    @abstractmethod
    def check_if_card_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):
        pass

    @abstractmethod
    def check_if_net_banking_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):
        pass

    @abstractmethod
    def check_if_upi_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):
        pass

    @abstractmethod
    def check_if_cash_on_delivery_payment_method_already_exists(self, payment_type:str):
        pass

    @abstractmethod
    def create_card_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        pass

    @abstractmethod
    def create_net_banking_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        pass

    @abstractmethod
    def create_upi_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        pass

    @abstractmethod
    def create_cash_on_delivery_payment_method(self, payment_type:str)->int:
        pass

    @abstractmethod
    def check_if_order_exists(self, order_id:int):
        pass

    @abstractmethod
    def check_if_payment_method_exists(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def add_payment_method_to_order(self, order_id:int, orderpayment_dto:OrderPaymentDTO)->int:
        pass

    @abstractmethod
    def check_if_item_properties_exists(self, properties:list[int]):
        pass

    @abstractmethod
    def delete_order(self, order_id:int):
        pass

    @abstractmethod
    def check_if_useraddress_exists(self, useraddress_id:int):
        pass

    @abstractmethod
    def update_user_address(self, useraddress_id:int, address_id:int):
        pass

    @abstractmethod
    def update_user_name(self, user_id:str, name:str):
        pass

    @abstractmethod
    def update_user_email(self, user_id:str, email:str):
        pass

    @abstractmethod
    def update_user_contact_number(self, user_id:str, contact_number:str):
        pass

    @abstractmethod
    def check_if_item_property_exists(self,itemproperty_id:int):
        pass

    @abstractmethod
    def delete_item_property(self, itemproperty_id:int):
        pass

    @abstractmethod
    def update_item_property(self, itemproperty_id:int, value:str):
        pass

    @abstractmethod
    def delete_user_address(self, useraddress_id:int):
        pass

    @abstractmethod
    def get_user_details(self,user_id:str)->dict:
        pass

    @abstractmethod
    def add_view_to_item(self, user_id:str, item_id:int)->int:
        pass

    @abstractmethod
    def get_item_details(self, item_id:int)->ItemDTO:
        pass
    
    @abstractmethod
    def check_if_cart_already_created_for_user(self, user_id:str):
        pass

    @abstractmethod
    def create_cart(self, user_id:str, name:str)->int:
        pass

    @abstractmethod
    def add_item_to_cart(self, cart_id:int, item_id:int, warranty_id:Optional[int], properties:list[int]):
        pass

    @abstractmethod
    def create_rating_for_item(self, item_id:int)->int:
        pass

    @abstractmethod
    def add_rating_to_item(self, item_id:int, rating:int):
        pass

    @abstractmethod
    def check_if_item_is_rated(self, item_id:int):
        pass

    @abstractmethod
    def get_item_rating(self, item_id:int)->float:
        pass

    @abstractmethod
    def check_if_emi_already_exists(self, emi_dto:EmiDTO):
        pass

    @abstractmethod
    def create_debit_card_emi(self, emi_dto:EmiDTO)->int:
        pass

    @abstractmethod
    def create_no_cost_emi(self, emi_dto:EmiDTO)->int:
        pass

    @abstractmethod
    def check_if_emi_exists(self, emi_id:int):
        pass

    @abstractmethod
    def add_emi_to_item(self, item_id:int, emi_id:int)->int:
        pass

    @abstractmethod
    def check_if_warranty_already_exists(self, warranty_name:str, warranty_amount:float, number_of_months:int):
        pass

    @abstractmethod
    def create_warrenty(self, warranty_name:str, warranty_amount:float, number_of_months:int):
        pass

    @abstractmethod
    def check_if_warranty_exists(self, warranty_id:int):
        pass

    @abstractmethod
    def add_warranty_to_item(self, item_id:int, warranty_id:int):
        pass