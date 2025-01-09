from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from amazon.constants import exception_messages


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_user_already_exists(self):
        raise BadRequest(*exception_messages.USER_ALREADY_EXISTS)
    
    def create_user(self, user_id:int):
        return {
            "user_id": user_id
        }
