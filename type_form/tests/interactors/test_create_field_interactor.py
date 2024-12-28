import pytest
from django_swagger_utils.drf_server.exceptions import NotFound,BadRequest
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.field_interactor import FieldInteractor
from type_form.exceptions.custom_exceptions import FieldAlreadyExistsException

class TestCreateFieldInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FieldInteractor(storage = self.storage, presenter = self.presenter)
    
    def test_field_already_exists_raises_exception(self):
        
        field_type = "TEXT"
        field_name = "My field"
        
        self.storage.check_if_field_already_exists.side_effect = FieldAlreadyExistsException
        self.presenter.raise_exception_for_field_already_exists.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_field(field_name = field_name,field_type = field_type)
            
        self.storage.check_if_field_already_exists.assert_called_once_with(field_type = field_type)
        self.presenter.raise_exception_for_field_already_exists.assert_called_once()
        
    def test_create_field(self):
        
        field_type = "TEXT"
        field_name = "My field"
        
        expected_output= {"id":1}
        
        self.storage.create_field.return_value = 1
        self.presenter.get_response_for_create_field.return_value = expected_output
        
        actual_output = self.interactor.create_field(field_name = field_name,field_type = field_type)
        
        assert actual_output == expected_output
        
        self.storage.check_if_field_already_exists.assert_called_once_with(field_type = field_type)
        self.storage.create_field.assert_called_once_with(field_name = field_name,field_type = field_type)
        self.presenter.get_response_for_create_field.assert_called_once_with(id = 1)