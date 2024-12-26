from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,MissingLabel,MissingFieldType,FieldAlreadyExists,InvalidForm
from type_form.interactors.storage_interfaces.storage_interface import Fielddto,FormFielddto

class FieldInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def create_field(self,form_id:int,label:str,field_type:str,is_required:bool):

        """
            ELP:
                check if input data exists
                check if form exists
                check if field exists
                add field to form
        """
        self.validate_input_data_for_create_field(label = label, field_type = field_type)

        try:
            self.storage.check_if_field_already_exists(label = label,field_type = field_type)
        except FieldAlreadyExists:
            self.presenter.raise_exception_for_field_already_exists()

        if is_required:
            fielddto = Fielddto(label = label,field_type = field_type,is_required = is_required)
        else:
            fielddto = Fielddto(label = label,field_type = field_type)

        field_id = self.storage.create_field(field_dto = field_dto)
        return self.presenter.get_response_for_create_field(id = field_id)

    def validate_input_data_for_create_field(self,label:str,field_type:str):

        try:
            self.storage.valid_label_field(label = label)
        except MissingLabel:
            self.presenter.raise_exception_for_missing_label()

        try:
            self.storage.valid_field_type_field(field_type = field_type)
        except MissingFieldType:
            self.presenter.raise_exception_for_missing_field_type()



    def add_fields_to_form(self,form_id:int,field_ids:int):
        """
            ELP:
                check if input data exists
                check if form exists
                check if fields exists
                add fields to form
        """
        self.validate_input_data_for_add_fields(form_id = form_id,field_id = field_id)

        try:
            self.storage.check_form(id = form_id)
        except InvalidForm:
            self.presenter.raise_exception_for_invalid_form()

        try:
            self.storage.check_field(id = field_id)
        except InvalidField:
            self.presenter.raise_exception_for_invalid_field()

        formdto = self.storage.get_form(id = form_id)
        fielddto = self.storage.get_field(id = field_id)

        formfielddto = FormFielddto(form = formdto,field = fielddto)

        self.storage.add_field_to_form(formfielddto = formfielddto)
        
        return self.presenter.get_response_for_add_field_to_form()
        
    def validate_input_data_for_add_fields(self,form_id:int,field_id:int):

        try:
            self.storage.valid_id_field(id = form_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.valid_id_field(id = field_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_fieldid()


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


    