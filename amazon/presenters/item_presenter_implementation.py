from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.constants import exception_messages
from amazon.interactors.storage_interfaces.dtos import ItemDTO, RatingDTO

class ItemPresenterImplementation(ItemPresenterInterface):

    def raise_exception_for_item_already_exists(self):
        raise BadRequest(*exception_messages.ITEM_ALREADY_EXISTS)
    
    def raise_exception_for_item_does_not_exist(self):
        raise NotFound(*exception_messages.ITEM_DOES_NOT_EXIST)
    
    def get_response_for_create_item(self, item_id:int):

        return {
            "item_id": item_id
        }
    
    def raise_exception_for_property_already_exists(self):
        raise BadRequest(*exception_messages.PROPERTY_ALREADY_EXISTS)
    
    def raise_exception_for_property_does_not_exist(self):
        raise NotFound(*exception_messages.PROPERTY_DOES_NOT_EXIST)
    
    def get_response_for_create_property(self, property_id:int):

        return {
            "property_id": property_id
        }
    
    def get_response_for_add_property_to_item(self, itemproperty_id):

        return {
            "itemproperty_id": itemproperty_id
        }
    
    def get_response_for_list_of_items(self, item_dtos:ItemDTO)->list[dict]:
        
        list_of_items = []

        for item_dto in item_dtos:
            item_dto = {
                "item_name": item_dto.item_name
            }
            list_of_items.append(item_dto)

        return list_of_items
    
    def get_response_for_list_of_items_by_category(self, item_dtos:ItemDTO)->list[dict]:
        
        list_of_items = []

        for item_dto in item_dtos:
            item_dto = {
                "item_name": item_dto.item_name
            }
            list_of_items.append(item_dto)

        return list_of_items
    
    def raise_exception_for_cart_already_created(self):
        raise BadRequest(*exception_messages.CART_ALREADY_CREATED)
    
    def raise_exception_for_cart_does_not_exist(self):
        raise NotFound(*exception_messages.CART_DOES_NOT_EXIST)
    
    def get_response_for_create_cart(self, cart_id:int):
        
        return {
            "cart_id": cart_id
        }
    
    def get_response_for_add_item_to_cart(self, cartitem_id):
        
        return {
            "success": "item added to cart"
        }
    
    def raise_exception_for_whishlist_already_created(self):
        raise BadRequest(*exception_messages.WHISHLIST_ALREADY_CREATED)
    
    def raise_exception_for_whishlist_does_not_exist(self):
        raise NotFound(*exception_messages.WHISHLIST_DOES_NOT_EXIST)
    
    def get_response_for_create_whishlist(self, whishlist_id:int):
        
        return {
            "whishlist_id": whishlist_id
        }
    
    def get_response_for_add_item_to_whishlist(self, whishlistitem_id):
        
        return {
            "success": "item added to whishlist"
        }
    
    def raise_exception_for_item_does_not_exist_in_whishlist(self):
        raise NotFound(*exception_messages.ITEM_DOES_NOT_EXIST_IN_WHISHLIST)
    
    def raise_exception_for_item_property_does_not_exist(self):
        raise NotFound(*exception_messages.ITEM_PROPERTY_DOES_NOT_EXIST)
    
    def get_response_for_rate_an_item(self, item_rating_id:int):
        
        return {
            "item_rating_id": item_rating_id
        }
    
    def raise_exception_for_user_already_rated_item(self):
        raise BadRequest(*exception_messages.USER_ALREADY_RATED_ITEM)
    
    def raise_exception_for_item_not_rated(self):
        raise NotFound(*exception_messages.ITEM_NOT_RATED)
    
    def get_response_for_ratings_of_an_item(self, rating_dtos:list[RatingDTO])->list[dict]:
        
        list_of_ratings = []

        for rating_dto in rating_dtos:
            rating_dto = {
                "user_id": rating_dto.user_id,
                "rating": rating_dto.rating
            }
            list_of_ratings.append(rating_dto)

        return list_of_ratings