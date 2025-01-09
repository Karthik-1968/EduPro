from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserDTO:
    id:str
    name:str
    email:str
    contact_number:str

@dataclass
class AddressDTO:
    door_no:str
    street:str
    city:str
    district:str
    state:str
    country:str
    pincode:str
    contact_number:str
    address_type:str

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
    address_id:int
    order_status:str
    delivery_date:str
    delivery_charges:Optional[float]
    receiving_person_name:Optional[str]
    item_warranty_id:Optional[int]=None
    item_properties:Optional[list[int]]=None
    item_id:Optional[int]=None
    cart_id:Optional[int]=None

@dataclass
class PaymentMethodDTO:
    payment_type:str
    card_name:Optional[str]=None
    card_number:Optional[str]=None
    card_holder_name:Optional[str]=None
    cvv:Optional[str]=None
    expiry_date:Optional[str]=None
    card_type:Optional[str]=None
    bank_name:Optional[str]=None
    username:Optional[str]=None
    password:Optional[str]=None
    upi_id:Optional[str]=None

@dataclass
class OrderPaymentDTO:
    order_id:int
    payment_method_id:int
    payment_status:str
    amount:int
    transaction_id:str
    gift_card_or_promo_code:Optional[str]

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
    card_name:str

@dataclass
class OfferDTO:
    offer_type:str
    offer_name:Optional[str]
    card_name:str
    discount_in_rupees:int
    discount_in_percentage:float
    minimum_purchase_value:Optional[float]
    minimum_months_emi:Optional[int]
    start_date:str
    end_date:str
    terms_and_conditions:str
    coupon_code:Optional[str]=None
    minimum_number_of_items:Optional[int]=None

@dataclass
class ItemsCartDTO:
    cart_id:int
    item_id:int
    item_properties:list[int]
    item_warranty_id:Optional[int]
    item_exchange_properties:Optional[list[int]]

class StorageInterface:

    @abstractmethod
    def check_if_user_already_exists(self, email:str, contact_number:str):
        pass

    @abstractmethod
    def create_user(self, user_dto:UserDTO)->str:
        pass

    @abstractmethod
    def check_if_address_already_exists(self, address_dto:AddressDTO):
        pass

    @abstractmethod
    def create_address(self, address_dto:AddressDTO)->int:
        pass

    @abstractmethod
    def check_if_user_exists(self, user_id:str):
        pass

    @abstractmethod
    def check_if_address_exists(self, address_id:int):
        pass

    @abstractmethod
    def check_if_address_already_added_to_user(self, user_id:str, address_id:int):
        pass

    @abstractmethod
    def add_address_to_user(self, user_id:str, address_id:int)->int:
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
    def create_item(self, item_dto:ItemDTO)->int:
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
    def create_order_for_item(self, order_dto:OrderDTO)->int:
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
    def check_if_cash_on_delivery_payment_method_already_exists(self, paymentmethod_dto:PaymentMethodDTO):
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
    def create_cash_on_delivery_payment_method(self, paymentmethod_dto:PaymentMethodDTO)->int:
        pass

    @abstractmethod
    def check_if_order_exists(self, order_id:int):
        pass

    @abstractmethod
    def check_if_payment_method_exists(self, payment_method_id:int):
        pass

    @abstractmethod
    def add_payment_method_to_order(self, orderpayment_dto:OrderPaymentDTO)->int:
        pass

    @abstractmethod
    def check_if_item_properties_exists(self, item_properties:list[int]):
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
    def check_if_item_property_exists(self,item_property_id:int):
        pass

    @abstractmethod
    def delete_item_property(self, item_property_id:int):
        pass

    @abstractmethod
    def update_item_property(self, item_property_id:int, value:str):
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
    def add_item_to_cart(self, itemscart_dto:ItemsCartDTO)->int:
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

    @abstractmethod
    def check_if_cart_exists(self, cart_id:int):
        pass

    @abstractmethod
    def create_order_for_cart(self, order_dto:OrderDTO)->int:
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
    def create_other_emi_type(self, emi_dto:EmiDTO)->int:
        pass

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
    def check_if_number_of_left_in_stock_is_greater_than_zero(self, item_id:int):
        pass

    @abstractmethod
    def check_if_item_warranty_exists(self, item_warranty_id:int):
        pass

    @abstractmethod
    def check_if_item_exchange_properties_exists(self, item_exchange_properties:list[int]):
        pass

    @abstractmethod
    def add_item_exchange_properties_to_order(self, order_id:int, item_exchange_properties:list[int]):
        pass

    @abstractmethod
    def check_if_item_is_in_cart(self, item_id:int, cart_id:int):
        pass

    @abstractmethod
    def delete_item_from_cart(self, item_id:int, cart_id:int):
        pass

    @abstractmethod
    def check_if_whishlist_already_created_for_user(self, user_id:str):
        pass

    @abstractmethod
    def create_whishlist_for_user(self, user_id:str, name:str)->int:
        pass

    @abstractmethod
    def get_recommendations_for_user(self, user_id:str)->list[int]:
        pass

    @abstractmethod
    def check_if_whishlist_exists(self, whishlist_id:int):
        pass

    @abstractmethod
    def add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):
        pass

    @abstractmethod
    def check_if_item_is_in_whishlist(self, item_id:int, whishlist_id:int):
        pass

    @abstractmethod
    def delete_item_from_whishlist(self, item_id:int, whishlist_id:int):
        pass

    @abstractmethod
    def get_list_best_selling_items(self)->list[int]:
        pass

    @abstractmethod
    def get_list_of_top_rated_items(self)->list[int]:
        pass

    @abstractmethod
    def get_recently_viewed_item_by_user(self, user_id:str)->int:
        pass

    @abstractmethod
    def check_if_user_viewed_any_item(self, user_id:str):
        pass
