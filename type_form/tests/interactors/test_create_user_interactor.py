from type_form.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from type_form.interactors.storage_interfaces.storage_interface import StorageInterface
from type_form.exceptions.custom_exceptions import UserAlreadyPresentException
import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from unittest.mock import Mock
from type_form.interactors.user_interactor import UserInteractor
    

class TestCreateUserInteractor:

    def setup_method(self):
        self.storage = Mock(spec=StorageInterface)
        self.presenter = Mock(spec=PresenterInterface)
        self.interactor = UserInteractor(storage=self.storage)


    def test_create_user_email_already_exists(self):
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        user_email = "kd@gmail.com"
        
        self.storage.check_if_user_already_present.side_effect = UserAlreadyPresentException
        self.presenter.raise_exception_for_user_already_present.side_effect = BadRequest
        
        with pytest.raises(BadRequest):
            self.interactor.create_user(id=user_id, email=user_email, presenter=self.presenter)

        self.storage.check_if_user_already_present.assert_called_once_with(email=user_email)
        self.presenter.raise_exception_for_user_already_present.assert_called_once()
        
    def test_create_user_success(self):
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        user_email = "kd@gmail.com"
        
        expected_output = {
            "email": user_email
        }
        
        self.storage.create_user.return_value = user_email
        self.presenter.get_response_for_create_user.return_value = expected_output

        actual_output = self.interactor.create_user(id=user_id, email=user_email, presenter=self.presenter)

        assert actual_output == expected_output
        
        self.storage.check_if_user_already_present.assert_called_once_with(email=user_email)
        self.storage.create_user.assert_called_once_with(id=user_id, email=user_email)
        self.presenter.get_response_for_create_user.assert_called_once_with(user_email=user_email)
        