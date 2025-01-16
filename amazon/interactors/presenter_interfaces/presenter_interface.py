from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import CategoryDTO, ItemDTO, OrderIdDTO, RatingDTO, ItemIdDTO

class PresenterInterface:

    @abstractmethod
    def raise_exception_for_user_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_user(self, user_id:str):
        pass

    @abstractmethod
    def raise_exception_for_address_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_address(self, address_id:str):
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
    def raise_exception_for_category_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_category(self, category_id:int):
        pass

    @abstractmethod
    def get_response_for_list_of_categories(self, category_dtos:list[CategoryDTO])->list[dict]:
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
    def raise_exception_for_property_already_exists(self):
        pass
    
    @abstractmethod
    def get_response_for_create_property(self, property_id:int):
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
    def get_response_for_create_order_for_item(self, order_id:int):
        pass

    @abstractmethod
    def get_response_for_get_orders_of_user(self, order_dtos:list[OrderIdDTO])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_get_orders_of_item(self, orderid_dtos:list[OrderIdDTO])->list[dict]:
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
    def get_response_for_add_payment_method_to_order(self, payment_id:int):
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
    def get_response_for_delete_order(self):
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
    def raise_exception_for_out_of_stock(self):
        pass

    @abstractmethod
    def get_response_for_add_view_to_item(self, no_of_views:int):
        pass

    @abstractmethod
    def get_response_for_get_item_details(self, item_dto:ItemDTO)->dict:
        pass

    @abstractmethod
    def raise_exception_for_cart_already_created(self):
        pass

    @abstractmethod
    def get_response_for_create_cart(self, cart_id:int):
        pass

    @abstractmethod
    def get_response_for_add_item_to_cart(self):
        pass

    @abstractmethod
    def get_response_for_rate_an_item(self, item_rating_id:int):
        pass

    @abstractmethod
    def raise_exception_for_item_not_rated(self):
        pass

    @abstractmethod
    def get_response_for_ratings_of_an_item(self, rating_dtos:list[RatingDTO])->list[dict]:
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
    def raise_exception_for_emi_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_emi_to_item(self, item_emi_id:int):
        pass

    @abstractmethod
    def raise_exception_for_warrenty_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_warranty(self, warranty_id:int):
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

    @abstractmethod
    def get_response_for_list_best_selling_items(self, best_selling_items:list[int])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_list_of_top_rated_items(self, top_rated_items:list[ItemIdDTO])->list[dict]:
        pass

    @abstractmethod
    def get_response_for_recently_viewed_item_by_user(self, recently_viewed_item:int)->dict:
        pass

    @abstractmethod
    def raise_exception_for_user_has_not_viewed_any_item(self):
        pass

    @abstractmethod
    def get_response_for_recommendations_for_multiple_users(self, recommendations_dtos:list[ItemDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_user_already_rated_item(self):
        pass

    @abstractmethod
    def get_response_for_create_refund_request(self, refund_id:int):
        pass

    @abstractmethod
    def raise_exception_for_refund_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_update_refund_status_after_refunded(self):
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
    def raise_exception_for_item_emi_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_item_emi_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_emi_already_added_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_emi_is_not_associated_with_item(self):
        pass

    @abstractmethod
    def raise_exception_for_item_emi_already_added_to_item_in_cart(self):
        pass

    @abstractmethod
    def get_response_for_add_item_emi_to_item_in_cart(self):
        pass

    @abstractmethod
    def raise_exception_for_item_warranty_is_not_associated_with_item(self):
        pass

    @abstractmethod
    def raise_exception_for_warranty_already_associated_with_order(self):
        pass

    @abstractmethod
    def get_response_for_add_item_warranty_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_offer_is_not_specific_to_item_in_order(self):
        pass

    @abstractmethod
    def raise_exception_for_offer_already_added_to_order(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_properties_are_already_added_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_properties_are_not_associated_with_item_in_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_property_does_not_belong_to_item(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_belong_to_cart(self):
        pass

    @abstractmethod
    def raise_exception_for_delivery_service_already_exists(self):
        pass