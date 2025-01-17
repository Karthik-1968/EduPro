import pytest
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions.user_custom_exceptions import UserAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.user_interactor import UserInteractor
from mock import create_autospec
from amazon.interactors.storage_interfaces.dtos import UserDTO

class TestCreateUserInteractor:

    def setup_method(self):

        self.storage = create_autospec(UserStorageInterface)
        self.interactor = UserInteractor(storage = self.storage)

    def test_if_user_already_exists_raises_exception(self):
        
        user_dto = UserDTO(
        id = "550e8400-e29b-41d4-a716-446655440000",
        name = "John Doe",
        email = "kd@gmail.com",
        contact_number = "9876543210")

        presenter = create_autospec(UserPresenterInterface)

        self.storage.check_if_user_already_exists.side_effect = UserAlreadyExistsException
        presenter.raise_exception_for_user_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_user(user_dto=user_dto, presenter=presenter)
        
        self.storage.check_if_user_already_exists.assert_called_once_with(email=user_dto.email, contact_number=user_dto.contact_number)
        presenter.raise_exception_for_user_already_exists.assert_called_once()

    def test_create_user(self):

        user_dto = UserDTO(
        id = "550e8400-e29b-41d4-a716-446655440000",
        name = "John Doe",
        email = "kd@gmail.com",
        contact_number = "9876543210")

        presenter = create_autospec(UserPresenterInterface)

        expected_output = {"user_id":id}

        self.storage.create_user.return_value = id
        presenter.get_response_for_create_user.return_value = expected_output

        actual_output = self.interactor.create_user(user_dto=user_dto, presenter=presenter)

        assert actual_output == expected_output

        self.storage.check_if_user_already_exists.assert_called_once_with(email=user_dto.email, contact_number=user_dto.contact_number)
        self.storage.create_user.assert_called_once_with(user_dto=user_dto)
        presenter.get_response_for_create_user.assert_called_once_with(user_id=id)