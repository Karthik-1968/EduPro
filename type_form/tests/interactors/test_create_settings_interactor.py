import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_field_settings_interactor import FormFieldSettingsInteractor
from type_form.exceptions.custom_exceptions import SettingsAlreadyExistsException

    
class TestCreateSettingsInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormFieldSettingsInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_settings_already_exists_raises_exception(self):
        
        multiple_selection = None
        multiple_selection_scope = None
        choices = None
        phone_number_choices = None
        max_number = None
        min_number = None
        max_length = 10
        min_length = 1
        other_option = None
        vetical_alignment = None
        alphabetical_order = None
        placeholder = "Enter First Name"
        
        self.storage.check_if_settings_exists.side_effect = SettingsAlreadyExistsException
        self.presenter.raise_exception_for_settings_already_exists.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_settings(multiple_selection = multiple_selection, multiple_selection_scope = multiple_selection_scope,\
                choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
                max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
                alphabetical_order = alphabetical_order, placeholder = placeholder)
            
        self.storage.check_if_settings_exists.assert_called_once_with(multiple_selection = multiple_selection, multiple_selection_scope = multiple_selection_scope,\
            choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
            max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
            alphabetical_order = alphabetical_order, placeholder = placeholder)
        
        self.presenter.raise_exception_for_settings_already_exists.assert_called_once()
        
    def test_create_settings(self):
        
        multiple_selection = None
        multiple_selection_scope = None
        choices = None
        phone_number_choices = None
        max_number = None
        min_number = None
        max_length = 10
        min_length = 1
        other_option = None
        vetical_alignment = None
        alphabetical_order = None
        placeholder = "Enter First Name"
        
        expected_settings_id = 1
        expected_output = {"id":1}
        
        self.storage.create_settings.return_value = expected_settings_id
        self.presenter.get_response_for_create_settings.return_value = expected_output
        
        actual_output = self.interactor.create_settings(multiple_selection = multiple_selection,\
            multiple_selection_scope = multiple_selection_scope,choices = choices, phone_number_choices = phone_number_choices,\
            max_number = max_number, min_number = min_number,max_length = max_length, min_length = min_length, \
            other_option = other_option, vetical_alignment = vetical_alignment,alphabetical_order = alphabetical_order, \
                placeholder = placeholder)
        
        assert actual_output == expected_output
        
        self.storage.check_if_settings_exists.assert_called_once_with(multiple_selection = multiple_selection,\
            multiple_selection_scope = multiple_selection_scope,\
            choices = choices, phone_number_choices = phone_number_choices, max_number = max_number, min_number = min_number,\
            max_length = max_length, min_length = min_length, other_option = other_option, vetical_alignment = vetical_alignment,\
            alphabetical_order = alphabetical_order, placeholder = placeholder)
        
        self.storage.create_settings.assert_called_once_with(multiple_selection = multiple_selection, \
            multiple_selection_scope = multiple_selection_scope, choices = choices, phone_number_choices = phone_number_choices,\
            max_number = max_number, min_number = min_number, max_length = max_length, min_length = min_length, \
            other_option = other_option, vetical_alignment = vetical_alignment, alphabetical_order = alphabetical_order, \
                placeholder = placeholder)
        
        self.presenter.get_response_for_create_settings.assert_called_once_with(id = expected_settings_id)
    
    