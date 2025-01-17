from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import ItemDTO, ItemIdDTO, EmiDTO, ItemsCartDTO, RatingDTO

class ItemStorageInterface:

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
    def check_if_item_properties_exists(self, item_properties:list[int]):
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
    def rate_an_item(self, item_id:int, user_id:str, rating:str)->int:
        pass

    @abstractmethod
    def check_if_item_is_rated(self, item_id:int):
        pass

    @abstractmethod
    def get_ratings_of_an_item(self, item_id:int)->list[RatingDTO]:
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
    def add_emi_to_order(self, order_id:int, emi_id:int):
        pass

    @abstractmethod
    def create_other_emi_type(self, emi_dto:EmiDTO)->int:
        pass

    @abstractmethod
    def check_if_number_of_left_in_stock_is_greater_than_zero(self, item_id:int):
        pass

    @abstractmethod
    def check_if_item_warranty_exists(self, item_warranty_id:int):
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
    def get_recommendations_for_user(self, user_id:str)->list[ItemIdDTO]:
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
    def get_list_best_selling_items(self)->list[ItemIdDTO]:
        pass

    @abstractmethod
    def get_list_of_top_rated_items(self)->list[ItemIdDTO]:
        pass

    @abstractmethod
    def get_recently_viewed_item_by_user(self, user_id:str)->int:
        pass

    @abstractmethod
    def check_if_user_viewed_any_item(self, user_id:str):
        pass

    @abstractmethod
    def check_if_user_already_rated_item(self, item_id:int, user_id:str):
        pass

    @abstractmethod
    def check_if_item_emi_exists(self, item_emi_id:int):
        pass

    @abstractmethod
    def check_if_item_emi_is_associated_with_item(self, item_emi_id:int, order_id:int):
        pass

    @abstractmethod
    def check_if_item_emi_is_not_already_added_to_order(self, order_id:int, item_emi_id:int):
        pass

    @abstractmethod
    def add_item_emi_to_order(self, order_id:int, item_emi_id:int):
        pass

    @abstractmethod
    def check_if_item_emi_is_already_added_to_item_in_cart(self, item_id:int, item_emi_id:int):
        pass

    @abstractmethod
    def add_item_emi_to_item_in_cart(self, item_id:int, order_id:int, item_emi_id:int):
        pass

    @abstractmethod
    def check_if_item_warranty_is_associated_with_item(self, item_id:int, item_warranty_id:int):
        pass

    @abstractmethod
    def check_if_item_warranty_is_already_associated_with_order(self, order_id:int, item_warranty_id:int):
        pass

    @abstractmethod
    def add_item_warranty_to_order(self, order_id:int, item_warranty_id:int):
        pass

    @abstractmethod
    def check_if_items_exists(self, item_ids:list[int]):
        pass

    @abstractmethod
    def check_if_item_properties_belong_to_item(self, item_properties:list[int], item_id:int):
        pass

    @abstractmethod
    def check_if_items_are_in_cart(self, item_ids:list[int], cart_id:int):
        pass