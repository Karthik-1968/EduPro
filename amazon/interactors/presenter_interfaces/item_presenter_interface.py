from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import ItemDTO, RatingDTO, ItemIdDTO

class ItemPresenterInterface:

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
    def raise_exception_for_item_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_delete_item_property(self):
        pass

    @abstractmethod
    def get_response_for_update_item_property(self):
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
    def get_response_for_add_emi_to_order(self):
        pass

    @abstractmethod
    def get_response_for_create_other_emi_type(self, emi_id:int):
        pass

    @abstractmethod
    def raise_exception_for_item_warranty_does_not_exist(self):
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
    def raise_exception_for_item_warranty_already_associated_with_order(self):
        pass

    @abstractmethod
    def get_response_for_add_item_warranty_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_property_does_not_belong_to_item(self):
        pass

    @abstractmethod
    def raise_exception_for_item_does_not_belong_to_cart(self):
        pass

    