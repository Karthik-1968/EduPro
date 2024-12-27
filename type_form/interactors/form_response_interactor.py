from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import InvalidFormException, InvalidUserException
from type_form.interactors.storage_interfaces.storage_interface import FormResponsedto
import uuid


class FormResponseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage=storage
        self.presenter=presenter

    def create_form_response(self, user_id:uuid, form_id:int, data:str, device:str, status:str):

        """ELP:
            -validate input data
                -validate user_id
                -validate form_id
                -validate data
                -validate device
                -validate status
            -check if user exists
            -check if form exists
            -create form response 
        """
        self.validate_input_data(user_id = user_id, form_id = form_id, data = data, device = device, status = status)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        userdto = self.storage.get_user(id = user_id)
        formdto = self.storage.get_form(id = form_id)

        formresponsedto = FormResponsedto(user = userdto,form = formdto, data = data, device = device,status = status)

        formresponse_id = self.storage.create_form_response(formresponsedto = formresponsedto)
        
        return self.presenter.get_response_for_create_form_response(id = formresponse_id)

    def validate_input_data(self, user_id:uuid, form_id:int, data:str, device:str, status:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()
        
        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()

        data_not_present = not data
        if data_not_present:
            self.presenter.raise_exception_for_missing_data()

        device_not_present = not device
        if device_not_present:
            self.presenter.raise_exception_for_missing_device()

        status_not_present = not status
        if status_not_present:
            self.presenter.raise_exception_for_missing_status()


    def get_responses_of_form(self,form_id:int):

        """
            ELP:
                -validate input data
                    -validate form_id
                -check if form exists
                -get responses of the form
        """
        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        formresponsedtos = self.storage.get_responses_of_form(id = form_id)

        return self.presenter.get_response_for_responses_of_form(formresponsedtos = formresponsedtos)