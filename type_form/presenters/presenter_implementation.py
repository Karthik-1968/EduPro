from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from type_form.constants.exception_messages import MISSING_EMAIL

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_missing_email(self):
        raise BadRequest(*MISSING_EMAIL)

    def raise_exception_for_invalid_user(self):
        raise BadRequest(*INVALID_USER)

    def get_response_for_create_user(self):
        return {
            "success":"user is created successfully"
        }