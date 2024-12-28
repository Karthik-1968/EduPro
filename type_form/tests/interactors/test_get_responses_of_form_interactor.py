import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from mock import create_autospec

from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.form_response_interactor import FormResponseInteractor
from type_form.exceptions.custom_exceptions import InvalidFormException
from type_form.interactors.storage_interfaces.storage_interface import FormResponsedto

class TestGetResponsesOfFormInteractor:
    
    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = FormResponseInteractor(storage = self.storage, presenter = self.presenter)
        
    def test_given_invalid_form_id_raises_exception(self):
        
        form_id = 1
        
        self.storage.check_form.side_effect = InvalidFormException
        self.presenter.raise_exception_for_invalid_form.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_responses_of_form(form_id = form_id)
            
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.presenter.raise_exception_for_invalid_form.assert_called_once()
        
    def test_get_responses_of_form(self):
        
        form_id = 1
        
        formresponse_dtos= [
            FormResponsedto(
                form_id = 1,
                user_id = "550e8400-e29b-41d4-a716-446655440000",
                data={
                    "name": "John",
                    "age": 25
                },
                device = "mobile",
                status = "SUBMITTED"
            ),
            FormResponsedto(
                form_id = 1,
                user_id = "550e8400-e29b-41d4-a716-446655440000",
                data={
                    "name": "Jack",
                    "age": 30
                },
                device = "mobile",
                status = "SUBMITTED"
            )
        ]
        expected_output= [
            {
                "user_id": "550e8400-e29b-41d4-a716-446655440000",
                "data": {
                    "name": "John",
                    "age": 25
                },
                "device": "mobile",
                "status": "SUBMITTED"
            },
            {
                "user_id": "550e8400-e29b-41d4-a716-446655440000",
                "data": {
                    "name": "Jack",
                    "age": 30
                },
                "device": "mobile",
                "status": "SUBMITTED"
            }
        ]
        
        self.storage.get_responses_of_form.return_value = formresponse_dtos
        self.presenter.get_response_for_responses_of_form.return_value = expected_output
        
        actual_output = self.interactor.get_responses_of_form(form_id = form_id)
        
        assert actual_output == expected_output
        
        self.storage.check_form.assert_called_once_with(id = form_id)
        self.storage.get_responses_of_form.assert_called_once_with(id = form_id)
        self.presenter.get_response_for_responses_of_form.assert_called_once_with(formresponse_dtos = formresponse_dtos)