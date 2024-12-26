from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,InvalidForm,InvalidUser,MissingData,MissingDevice
from type_form.interactors.storage_interfaces.storage_interface import FormResponsedto

class GetResponsesOfFormInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def get_responses_of_form(self,form_id:int):

        """
            ELP:
                check if input data exists
                check if form exists
                get responses of the form
        """
        try:
            self.storage.valid_id_field(id = form_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.check_form(id = form_id)
        except InvalidForm:
            self.presenter.raise_exception_for_invalid_form()

        formresponsedtos = self.storage.get_responses_of_form(id = form_id)

        return self.presenter.get_response_for_responses_of_form(formresponsedtos = formresponsedtos)