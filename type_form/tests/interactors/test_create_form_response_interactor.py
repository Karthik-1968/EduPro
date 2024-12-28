import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_response_interactor import FormResponseInteractor
from type_form.exceptions.custom_exceptions import InvalidFormException,InvalidUserException
from type_form.interactors.storage_interfaces.storage_interface import Fielddto

class TestCreateFormResponseInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormResponseInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_form_id_raises_exception(self):
        
        form_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        data={
            "name": "John",
            "age": 25
        }

        device = "mobile"
        status = "SUBMITTED"
        
        self.storage.check_form.side_effect = InvalidFormException
        self.presenter.raise_exception_for_invalid_form.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_form_response(form_id = form_id, user_id = user_id, data = data, device = device,\
                status = status)
            
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.presenter.raise_exception_for_invalid_form.assert_called_once()
        
    def test_given_invalid_user_id_raises_exception(self):
        
        form_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        data={
            "name": "John",
            "age": 25
        }

        device = "mobile"
        status = "SUBMITTED"
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.create_form_response(form_id = form_id, user_id = user_id, data = data, device = device,\
                status = status)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_create_form_response(self):
        
        form_id = 1
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        data={
            "name": "John",
            "age": 25
        }

        device = "mobile"
        status = "SUBMITTED"
        
        formresponse_id= 1
        expected_output= {"formresponse_id": 1}
        
        self.storage.create_form_response.return_value = formresponse_id
        self.presenter.get_response_for_create_form_response.return_value = expected_output
        
        actual_output = self.interactor.create_form_response(form_id = form_id, user_id = user_id, data = data, device = device,\
            status = status)
        
        assert actual_output == expected_output
        
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.storage.create_form_response.assert_called_once_with(form_id = form_id, user_id = user_id, data = data,\
            device = device, status = status)
        self.presenter.get_response_for_create_form_response.assert_called_once_with(id = formresponse_id)