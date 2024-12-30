import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_field_settings_interactor import FormFieldSettingsInteractor
from type_form.exceptions.custom_exceptions import SettingsAlreadyExistsException, InvalidFormFieldException,InvalidSettingsException

class TestAddSettingsToFormFieldInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormFieldSettingsInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_form_field_raises_exception(self):
        
        form_field_id = 1
        settings_id = 1
        
        self.storage.check_form_field.side_effect = InvalidFormFieldException
        self.presenter.raise_exception_for_invalid_form_field.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.add_settings_to_form_field(form_field_id = form_field_id, settings_id = settings_id)
            
        self.storage.check_form_field.assert_called_once_with(form_field_id = form_field_id)
        self.presenter.raise_exception_for_invalid_form_field.assert_called_once()
        
    def test_given_invalid_settings_raises_exception(self):
        
        form_field_id = 1
        settings_id = 1
        
        self.storage.check_settings.side_effect = InvalidSettingsException
        self.presenter.raise_exception_for_invalid_settings.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.add_settings_to_form_field(form_field_id = form_field_id, settings_id = settings_id)
            
        self.storage.check_settings.assert_called_once_with(settings_id = settings_id)
        self.presenter.raise_exception_for_invalid_settings.assert_called_once()
        
    def test_add_settings_to_form_field(self):
        
        form_field_id = 1
        settings_id = 1
        
        expected_output= {
            "success":"settings added to form field successfully"
        }
        
        self.storage.add_settings_to_form_field.return_value = None
        self.presenter.get_response_for_add_settings_to_form_field.return_value = expected_output
        
        actual_output = self.interactor.add_settings_to_form_field(form_field_id = form_field_id, settings_id = settings_id)
        
        assert actual_output == expected_output
        
        self.storage.check_form_field.assert_called_once_with(form_field_id = form_field_id)
        self.storage.check_settings.assert_called_once_with(settings_id = settings_id)
        self.storage.add_settings_to_form_field.assert_called_once_with(form_field_id = form_field_id, settings_id = settings_id)
        self.presenter.get_response_for_add_settings_to_form_field.assert_called_once_with()