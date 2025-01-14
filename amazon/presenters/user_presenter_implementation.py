from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.constants import exception_messages

class UserPresenterImplementation(UserPresenterInterface):

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
    

