from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface

from type_form.exceptions.custom_exceptions import FieldAlreadyExistsException, InvalidFormException, InvalidFieldException,\
    InvalidUserException
import uuid


class FieldInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_field(self, field_name:str, field_type:str):

        """
            ELP:
                -validate input data
                    -validate name
                    -validate field_type
                -check if field exists
                -add field to form
        """
        self.validate_input_data_for_create_field(field_name = field_name, field_type = field_type)

        try:
            self.storage.check_if_field_already_exists(field_type = field_type)
        except FieldAlreadyExistsException:
            self.presenter.raise_exception_for_field_already_exists()

        field_id = self.storage.create_field(field_name = field_name, field_type = field_type)
        
        return self.presenter.get_response_for_create_field(id = field_id)

    def validate_input_data_for_create_field(self, field_name:str, field_type:str):
        
        field_name_not_present = not field_name
        if field_name_not_present:
            self.presenter.raise_exception_for_missing_field_name()

        field_type_not_present = not field_type
        if field_type_not_present:
            self.presenter.raise_exception_for_missing_field_type()



    def add_field_to_form(self, form_id:int, user_id:uuid, field_id:int, label:str, is_required:bool=False):
        """
            ELP:
                -validate input data
                    -validate form_id
                    -validate user_id
                    -validate field_id
                    -validate label
                -check if form exists
                -check if user exists
                -check if fields exists
                -add fields to form
        """
        self.validate_input_data_for_add_fields(form_id = form_id, user_id = user_id, field_id = field_id, label = label)

        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        try:
            self.storage.check_user(id = user_id)
        except InvalidUserException:
            self.presenter.raise_exception_for_invalid_user()
        
        try:
            self.storage.check_field(id = field_id)
        except InvalidFieldException:
            self.presenter.raise_exception_for_invalid_field()

        self.storage.add_field_to_form(form_id = form_id, user_id = user_id, field_id = field_id, label = label, \
            is_required = is_required)
        
        return self.presenter.get_response_for_add_field_to_form()
        
    def validate_input_data_for_add_fields(self, form_id:int, user_id:uuid, field_id:int, label:str):
        
        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_userid()
            
        field_id_not_present = not field_id
        if field_id_not_present:
            self.presenter.raise_exception_for_missing_fieldid()
            
        label_not_present = not label
        if label_not_present:
            self.presenter.raise_exception_for_missing_formfield_label()


    def get_fields_of_form(self,form_id:int):

        """
            ELP:
                -validate input data
                    -validate form_id
                check if form exists
                get fields of form
        """

        form_id_not_present = not form_id
        if form_id_not_present:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.check_form(id = form_id)
        except InvalidFormException:
            self.presenter.raise_exception_for_invalid_form()

        fielddtos=self.storage.get_fields_of_form(id = form_id)
        
        return self.presenter.get_response_for_fields_of_form(fielddtos = fielddtos)


    