from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.storage_interfaces.storage_interface import PhoneNumberFieldSettingsDTO
from type_form.exceptions.custom_exceptions import SettingsAlreadyExistsException, InvalidFormFieldException, \
    InvalidSettingsException

class FormFieldSettingsInteractor:
    
    def __init__(self,storage:StorageInterface,presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter
        
    def create_settings(self, multiple_selection:bool=None, multiple_selection_scope:list[str]=None, choices:list[str]=None,\
        phone_number_choices:list[PhoneNumberFieldSettingsDTO]=None, max_number:int=None, min_number:int=None,\
        max_length:int=None, min_length:int=None, other_option:bool=None, vetical_alignment:bool=None,\
        alphabetical_order:bool=None, placeholder:str=None):
        """
            ELP:
                -check if settings exists
                -create settings
        """
        try:
            self.storage.check_if_settings_exists(multiple_selection = multiple_selection, multiple_selection_scope = multiple_selection_scope,\
                choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
                max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
                alphabetical_order = alphabetical_order, placeholder = placeholder)
        except SettingsAlreadyExistsException:
            self.presenter.raise_exception_for_settings_already_exists()
        
        settings_id = self.storage.create_settings(multiple_selection = multiple_selection, multiple_selection_scope = multiple_selection_scope,\
            choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
            max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
            alphabetical_order = alphabetical_order, placeholder = placeholder)
        
        return self.presenter.get_response_for_create_settings(id = settings_id)
    
    def add_settings_to_form_field(self, form_field_id:int, settings_id:int):
        """
            ELP:
                -check if form_field exists
                -check if settings exists
                -add settings to form_field
        """
        self.validate_input_data_for_add_settings_to_form_field(form_field_id = form_field_id, settings_id = settings_id)
        
        try:
            self.storage.check_form_field(form_field_id = form_field_id)
        except InvalidFormFieldException:
            self.presenter.raise_exception_for_invalid_form_field()
            
        try:
            self.storage.check_settings(settings_id = settings_id)
        except InvalidSettingsException:
            self.presenter.raise_exception_for_invalid_settings()
        
        self.storage.add_settings_to_form_field(form_field_id = form_field_id, settings_id = settings_id)
        
        return self.presenter.get_response_for_add_settings_to_form_field()
    
    def validate_input_data_for_add_settings_to_form_field(self, form_field_id:int, settings_id:int):
        
        form_field_id_not_present = not form_field_id
        if form_field_id_not_present:
            self.presenter.raise_exception_for_missing_form_field_id()
        
        settings_id_not_present = not settings_id
        if settings_id_not_present:
            self.presenter.raise_exception_for_missing_settings_id()