from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from amazon.interactors.address_interactor import AddressInteractor
from mock import create_autospec
import pytest

class TestAddAddressToUserInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.interactor = AddressInteractor(storage = self.storage)

    def test_if_user_does_not_exist_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        presenter = create_autospec(PresenterInterface)

        self.storage.check_if_user_exists.side_effect = custom_exceptions.UserDoesNotExistException
        presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id, presenter=presenter)
        
        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_address_does_not_exist_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        presenter = create_autospec(PresenterInterface)

        self.storage.check_if_address_exists.side_effect = custom_exceptions.AddressDoesNotExistException
        presenter.raise_exception_for_address_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id, presenter=presenter)
        
        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        presenter.raise_exception_for_address_does_not_exist.assert_called_once()

    def test_if_address_already_added_to_user_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        presenter = create_autospec(PresenterInterface)

        self.storage.check_if_address_already_added_to_user.side_effect = custom_exceptions.AddressAlreadyAddedToUserException
        presenter.raise_exception_for_address_already_added_to_user.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id, presenter=presenter)
        
        self.storage.check_if_address_already_added_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        presenter.raise_exception_for_address_already_added_to_user.assert_called_once()

    def test_add_address_to_user(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        presenter = create_autospec(PresenterInterface)

        useraddress_id = 1
        expected_output = {"useraddress_id":useraddress_id}

        self.storage.add_address_to_user.return_value = useraddress_id
        presenter.get_response_for_add_address_to_user.return_value = expected_output

        actual_output = self.interactor.add_address_to_user(user_id=user_id, address_id=address_id, presenter=presenter)

        assert actual_output == expected_output

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        self.storage.check_if_address_already_added_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        self.storage.add_address_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        presenter.get_response_for_add_address_to_user.assert_called_once_with(useraddress_id=useraddress_id)