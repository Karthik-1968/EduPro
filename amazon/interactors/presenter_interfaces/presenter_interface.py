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
    def raise_exception_for_missing_door_no(self):
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
    def get_response_for_create_order_for_item(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_get_orders_of_user(self, order_dtos:list[OrderDTO])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_get_orders_of_item(self, order_dtos:list[OrderDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_card_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_net_banking_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_upi_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_cash_on_delivery_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_payment_method_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_order_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_order_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_payment_method_id(self):
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
    def get_response_for_add_payment_method_to_order(self, payment_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_properties(self):
        pass

    @abstractmethod
    def get_response_for_create_card_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def get_response_for_create_net_banking_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def get_response_for_create_upi_payment_method(self, paymentmethod_id:int):
        pass
    
    @abstractmethod
    def get_response_for_create_cash_on_delivery_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_payment_type(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_upi_id(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_card_holder_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_card_number(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_expiry_date(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_cvv(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_bank_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_username(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_password(self):
        pass

    @abstractmethod
    def get_response_for_delete_order(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_useraddress_id(self):
        pass

    @abstractmethod
    def raise_exception_for_useraddress_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_update_user_address(self):
        pass

    @abstractmethod
    def get_response_for_update_user_name(self):
        pass

    @abstractmethod
    def get_response_for_update_email(self):
        pass

    @abstractmethod
    def get_response_for_update_user_contact_number(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_item_property_id(self):
        pass

    @abstractmethod
    def raise_exception_for_item_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_delete_item_property(self):
        pass

    @abstractmethod
    def get_response_for_update_item_property(self):
        pass

    @abstractmethod
    def get_response_for_delete_user_address(self):
        pass

    @abstractmethod
    def get_response_for_get_user_details(self,user_details:dict,order_details:list[dict])->dict:
        pass

    @abstractmethod
    def get_response_for_update_user_email(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_number_of_left_in_stock(self):
        pass

    @abstractmethod
    def raise_exception_for_out_of_stock(self):
        pass

    @abstractmethod
    def get_response_for_add_view_to_item(self, no_of_views:int):
        pass

    @abstractmethod
    def get_response_for_get_item_details(self, item_dto:ItemDTO)->dict:
        pass

    @abstractmethod
    def raise_exception_for_missing_cart_name(self):
        pass

    @abstractmethod
    def raise_exception_for_cart_already_created(self):
        pass

    @abstractmethod
    def get_response_for_create_cart(self, cart_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_cart_id(self):
        pass

    @abstractmethod
    def get_response_for_add_item_to_cart(self):
        pass

    @abstractmethod
    def get_response_for_create_rating_for_item(self, item_rating_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_rating(self):
        pass

    @abstractmethod
    def get_response_for_add_rating_to_item(self):
        pass

    @abstractmethod
    def raise_exception_for_item_not_rated(self):
        pass

    @abstractmethod
    def get_response_for_get_item_rating(self, item_rating:float):
        pass

    @abstractmethod
    def raise_exception_for_missing_card_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_emi_type(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_debit_card_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_number_of_months(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_interest_in_rupees(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_interest_in_percentage(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_total_amount(self):
        pass

    @abstractmethod
    def raise_exception_for_emi_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_debit_card_emi(self, emi_id:int):
        pass

    @abstractmethod
    def get_response_for_create_no_cost_emi(self, emi_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_emi_id(self):
        pass

    @abstractmethod
    def raise_exception_for_emi_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_emi_to_item(self, item_emi_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_warranty_name(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_warranty_amount(self):
        pass

    @abstractmethod
    def raise_exception_for_missing_number_of_months(self):
        pass

    @abstractmethod
    def raise_exception_for_warrenty_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_warranty(self, warranty_id:int):
        pass

    @abstractmethod
    def raise_exception_for_missing_warranty_id(self):
        pass

    @abstractmethod
    def raise_exception_for_warranty_does_not_exists(self):
        pass

    @abstractmethod
    def get_response_for_add_warranty_to_items(self, item_warranty_id:int):
        pass

    @abstractmethod
    def raise_exception_for_cart_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_create_order_for_cart(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_add_emi_to_order(self):
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
    def get_response_for_create_other_emi_type(self, emi_id:int):
        pass

    @abstractmethod
    def raise_exception_for_offer_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_bank_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_no_cost_emi_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_coupon_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_partner_offer(self, offer_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_property_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_exchange_property(self, exchange_property_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_value_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_exchange_value(self, exchange_value_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_value_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_exchange_value(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_item(self, item_exchange_property_id:int):
        pass

    @abstractmethod
    def raise_exception_for_offer_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_offer_to_item(self, item_offer_id:int):
        pass

    @abstractmethod
    def get_response_for_add_offer_to_order(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_warranty_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_item_exchange_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_item_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_exist_in_cart(self):
        pass

    @abstractmethod
    def get_response_for_delete_item_from_cart(self):
        pass

    @abstractmethod
    def raise_exception_for_whishlist_already_created(self):
        pass

    @abstractmethod
    def get_response_for_create_whishlist_for_user(self, whishlist_id:int):
        pass

    @abstractmethod
    def get_response_for_get_recommendations_for_user(self, recommendations:list[int])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_whishlist_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_item_to_whishlist(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_exist_in_whishlist(self):
        pass

    @abstractmethod
    def get_response_for_delete_item_from_whishlist(self):
        pass