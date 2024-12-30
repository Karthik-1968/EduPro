import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.field_interactor import FieldInteractor
from type_form.exceptions.custom_exceptions import InvalidFormException
from type_form.interactors.storage_interfaces.storage_interface import FieldDTO

class TestGetFieldsOfForm:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FieldInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_form_id_raises_exception(self):
        
        form_id = 1
        
        self.storage.check_form.side_effect = InvalidFormException
        self.presenter.raise_exception_for_invalid_form.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_fields_of_form(form_id = form_id)
            
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.presenter.raise_exception_for_invalid_form.assert_called_once()
        
    def test_get_fields_of_form(self):
        
        form_id = 1
        
        expected_fielddto= [FieldDTO(field_type = "TEXT", field_name = "My field")]
        expected_output= [{"field_type":"TEXT","field_name":"My field"}]
        
        self.storage.get_fields_of_form.return_value = expected_fielddto
        self.presenter.get_response_for_fields_of_form.return_value = expected_output
        
        actual_output = self.interactor.get_fields_of_form(form_id = form_id)
        
        assert actual_output == expected_output
        
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.storage.get_fields_of_form.assert_called_once_with(id = form_id)
        self.presenter.get_response_for_fields_of_form.assert_called_once_with(fielddtos = expected_fielddto)