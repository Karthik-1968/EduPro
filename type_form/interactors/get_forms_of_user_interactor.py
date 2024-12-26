from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,InvalidUser
from type_form.interactors.storage_interfaces.storage_interface import Formdto

class GetFormsOfUserInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def get_forms_of_user(self,user_id:uuid):

        """
            ELP:
                check if input data exists
                check if user exists
                get list of forms of user
        """

        try:
            self.storage.valid_userid_field(id = user_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_userid()

        try:
            self.storage.check_user(id = user_id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        formdtos=self.storage.get_forms_of_user(id = user_id)
        return self.presenter.get_response_for_forms_of_user(formdtos=formdtos)