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
class OrderItemDTO:
    user_id:str
    address_id:int
    order_status:str
    delivery_date:str
    item_properties:list[int]
    item_id:int
    delivery_charges:Optional[float]
    receiving_person_name:Optional[str]

@dataclass
class OrderCartItemsDTO:
    user_id:str
    address_id:int
    order_status:str
    delivery_date:str
    delivery_charges:Optional[float]
    receiving_person_name:Optional[str]
    item_ids: int
    cart_id:int

@dataclass
class CardPaymentMethodDTO:
    payment_type:str
    card_name:str
    card_number:str
    card_holder_name:str
    cvv:str
    expiry_date:str
    card_type:str

@dataclass
class NetBankingPaymentMethodDTO:
    payment_type:str
    bank_name:str
    username:str
    password:str

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

@dataclass
class OrderIdDTO:
    order_id:int

@dataclass
class RatingDTO:
    user_id:str
    rating:int

@dataclass
class ItemIdDTO:
    item_id:int

@dataclass
class RefundDTO:
    user_id:str
    order_id:int
    amount:float
    refund_status:str
    payment_date:int
    reason:str