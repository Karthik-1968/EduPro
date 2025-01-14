from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from amazon.constants import exception_messages
from amazon.interactors.storage_interfaces.dtos import CategoryDTO

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_user_already_exists(self):
        raise BadRequest(*exception_messages.USER_ALREADY_EXISTS)
    
    def raise_exception_for_user_does_not_exist(self):
        raise NotFound(*exception_messages.USER_DOES_NOT_EXIST)
    
    def get_response_for_create_user(self, user_id:int):
        return {
            "user_id": user_id
        }
    
    def raise_exception_for_address_already_exists(self):
        raise BadRequest(*exception_messages.ADDRESS_ALREADY_EXISTS)
    
    def raise_exception_for_address_does_not_exist(self):
        raise NotFound(*exception_messages.ADDRESS_DOES_NOT_EXIST)
    
    def get_response_for_create_address(self, address_id:int):
        return {
            "address_id": address_id
        }
    
    def raise_exception_for_address_already_added_to_user(self):
        raise BadRequest(*exception_messages.ADDRESS_ALREADY_ADDED_TO_USER)
    
    def get_response_for_add_address_to_user(self, useraddress_id):

        return {
            "useraddress_id": useraddress_id
        }
    
    def raise_exception_for_category_already_exists(self):
        raise BadRequest(*exception_messages.CATEGORY_ALREADY_EXISTS)
    
    def raise_exception_for_category_does_not_exist(self):
        raise NotFound(*exception_messages.CATEGORY_DOES_NOT_EXIST)
    
    def get_response_for_create_category(self, category_id:int):
        return {
            "category_id": category_id
        }
    
    def get_response_for_list_of_categories(self, category_dtos:CategoryDTO)->list[dict]:

        list_of_categories = []

        for category_dto in category_dtos:
            category_dto = {
                "category_name": category_dto.category_name
            }
            list_of_categories.append(category_dto)

        return list_of_categories
    
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
    
    def get_response_for_create_order_for_item(self, order_id:int):

        return {
            "order_id":order_id
        }
    
    def raise_exception_for_order_does_not_exist(self):
        raise NotFound(*exception_messages.ORDER_DOES_NOT_EXIST)
    
    def get_response_for_create_order_for_cart(self, order_id:int):

        return {
            "order_id":order_id
        }
    
    def get_response_for_create_card_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def raise_exception_for_payment_method_does_not_exist(self):
        raise NotFound(*exception_messages.PAYMENT_METHOD_DOES_NOT_EXIST)
    
    def get_response_for_create_netbanking_payment_method(self, paymentmethod_id:int):
        
        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def get_response_for_create_upi_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def get_response_for_create_cash_on_delivery_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def raise_exception_for_card_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.CARD_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_netbanking_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.NETBANKING_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_upi_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.UPI_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_cash_on_delivery_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.CASH_ON_DELIVERY_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def get_response_for_add_payment_method_to_order(self, payment_id:int):
        
        return {
            "payment_id": payment_id
        }
    
    def get_response_for_create_refund_request(self, refund_id:int):
        
        return {
            "refund_id": refund_id
        }
    
    def raise_exception_for_refund_request_does_not_exist(self):
        raise NotFound(*exception_messages.REFUND_REQUEST_DOES_NOT_EXIST)
    
    def get_response_for_update_refund_status_after_refunded(self):

        return {
            "success": "refund status updated successfully"
        }
