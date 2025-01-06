import pytest
from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserAlreadyExists
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.user_interactor import UserInteractor
from mock import create_autospec

class TestCreateUserInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = UserInteractor(storage = self.storage, presenter = self.presenter)

    def test_if_user_already_exists_raises_exception(self):
        
        id = "550e8400-e29b-41d4-a716-446655440000"
        name = "John Doe"
        email = "kd@gmail.com"
        contact_number = "9876543210"

        self.storage.check_if_user_already_exists.side_effect = UserAlreadyExists
        self.presenter.raise_exception_for_user_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_user(id=id, name=name, email=email, contact_number=contact_number)
        
        self.storage.check_if_user_already_exists.assert_called_once_with(email=email, contact_number=contact_number)
        self.presenter.raise_exception_for_user_already_exists.assert_called_once()

    def test_create_user(self):

        id = "550e8400-e29b-41d4-a716-446655440000"
        name = "John Doe"
        email = "kd@gmail.com"
        contact_number = "9876543210"

        expected_output = {"user_id":id}

        self.storage.create_user.return_value = id
        self.presenter.get_response_for_create_user.return_value = expected_output

        actual_output = self.interactor.create_user(id=id, name=name, email=email, contact_number=contact_number)

        assert actual_output == expected_output

        self.storage.check_if_user_already_exists.assert_called_once_with(email=email, contact_number=contact_number)
        self.storage.create_user.assert_called_once_with(id=id, name=name, email=email, contact_number=contact_number)
        self.presenter.get_response_for_create_user.assert_called_once_with(user_id=id)