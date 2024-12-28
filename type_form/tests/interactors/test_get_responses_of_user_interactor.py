import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_response_interactor import FormResponseInteractor
from type_form.exceptions.custom_exceptions import InvalidUserException
from type_form.interactors.storage_interfaces.storage_interface import FormResponsedto

class TestGetResponsesOfUserInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormResponseInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_user_id_raises_exception(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        
        self.storage.check_user.side_effect = InvalidUserException
        self.presenter.raise_exception_for_invalid_user.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_responses_of_user(user_id = user_id)
            
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.presenter.raise_exception_for_invalid_user.assert_called_once()
        
    def test_get_responses_of_user(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        
        expected_formresponse_dto= [
            FormResponsedto(
                form_id = 1, 
                user_id = "550e8400-e29b-41d4-a716-446655440000",
                data = {"name": "John", "age": 25}, 
                device = "mobile", 
                status = "SUBMITTED"
            )
        ]
        expected_output= [
            {
                "form_id":1,
                "data":{"name": "John", "age": 25},
                "device":"mobile",
                "status":"SUBMITTED"
             }
        ]
        
        self.storage.get_responses_of_user.return_value = expected_formresponse_dto
        self.presenter.get_response_for_responses_of_user.return_value = expected_output
        
        actual_output = self.interactor.get_responses_of_user(user_id = user_id)
        
        assert actual_output == expected_output
        
        self.storage.check_user.assert_called_once_with(id = user_id)
        self.storage.get_responses_of_user.assert_called_once_with(id = user_id)
        self.presenter.get_response_for_responses_of_user.assert_called_once_with(formresponse_dtos = expected_formresponse_dto)