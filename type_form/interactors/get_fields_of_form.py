from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingIdInvalidForm
from type_form.interactors.storage_interfaces.storage_interface import Fielddto

class GetFieldsOfFormInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def get_fields_of_form(self,id:int):

        """
            ELP:
                check if input data exists
                check if form exists
                get fields of form
        """

        try:
            self.storage.valid_id_field(id = id)
        except MissingId:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.check_form(id = id)
        except InvalidForm:
            self.presenter.raise_exception_for_invalid_form()

        fielddtos=self.storage.get_fields_of_form(id = id)
        return self.presenter.get_response_for_fields_of_form(fielddtos = fielddtos)