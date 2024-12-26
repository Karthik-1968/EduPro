from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import MissingId,InvalidForm
from type_form.interactors.storage_interfaces.storage_interface import FormFielddto

class AddFieldToFormInteractor:

    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    def add_fields_to_form(self,form_id:int,field_ids:int):
        """
            ELP:
                check if input data exists
                check if form exists
                check if fields exists
                add fields to form
        """
        self.validate_input_data(form_id = form_id,field_id = field_id)

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
        
    def validate_input_data(self,form_id:int,field_id:int):

        try:
            self.storage.valid_id_field(id = form_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_formid()

        try:
            self.storage.valid_id_field(id = field_id)
        except MissingId:
            self.presenter.raise_exception_for_missing_fieldid()