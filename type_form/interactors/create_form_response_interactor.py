from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,InvalidForm,InvalidUser,MissingData,MissingDevice
from type_form.interactors.storage_interfaces.storage_interface import FormResponsedto
import uuid

class CreateFormResponseInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage=storage
        self.presenter=presenter

    def create_form_response(self,user_id:uuid,form_id:int,data:str,device:str):

        """ELP:
            check if input data exists
            check if user exists
            check if form exists
            create form response 
        """
        self.validate_input_data(user_id = user_id, form_id = form_id, data = data, device = device)

        try:
            self.storage.check_user(id = user_id)
        except InvalidUser:
            self.presenter.raise_exception_for_invalid_user()

        try:
            self.storage.check_form(id = form_id)
        except InvalidForm:
            self.presenter.raise_exception_for_invalid_form()

        userdto = self.storage.get_user(id = user_id)
        formdto = self.storage.get_form(id = form_id)

        fromresponsedto = FormResponsedto(user = userdto,form = formdto, data = data, device = device)

        formresponse_id = self.storage.create_form_response(formresponsedto = formresponsedto)
        return self.presenter.get_response_for_create_form_response(id = formresponse_id)

        def validata_input_data(self,user_id:uuid,form_id:int,data:str,device:str):

            try:
                self.storage.valid_userid_field(id = user_id)
            except MissingId:
                self.presenter.raise_exception_for_missing_userid()
            
            try:
                self.storage.valid_id_field(id = form_id)
            except MissingId:
                self.presenter.raise_exception_for_missing_formid()

            try:
                self.strorage.valid_data_field(data = data)
            except MissingData:
                self.presenter.raise_exception_for_missing_data()

            try:
                self.storage.valid_device_field(device = device)
            except MissingDevice:
                self.presenter.raise_exception_for_missing_device()