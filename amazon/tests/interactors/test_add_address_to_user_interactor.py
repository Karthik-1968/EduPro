from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExist, AddressDoesNotExist, AddressAlreadyAddedToUser
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from amazon.interactors.user_interactor import UserInteractor
from mock import create_autospec
import pytest

class TestAddAddressToUserInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = UserInteractor(storage = self.storage, presenter = self.presenter)

    def test_if_user_does_not_exist_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        self.storage.check_if_user_exists.side_effect = UserDoesNotExist
        self.presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id)
        
        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_address_does_not_exist_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        self.storage.check_if_address_exists.side_effect = AddressDoesNotExist
        self.presenter.raise_exception_for_address_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id)
        
        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        self.presenter.raise_exception_for_address_does_not_exist.assert_called_once()

    def test_if_address_already_added_to_user_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        self.storage.check_if_address_already_added_to_user.side_effect = AddressAlreadyAddedToUser
        self.presenter.raise_exception_for_address_already_added_to_user.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_address_to_user(user_id=user_id, address_id=address_id)
        
        self.storage.check_if_address_already_added_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        self.presenter.raise_exception_for_address_already_added_to_user.assert_called_once()

    def test_add_address_to_user(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        address_id = 1

        useraddress_id = 1
        expected_output = {"useraddress_id":useraddress_id}

        self.storage.add_address_to_user.return_value = useraddress_id
        self.presenter.get_response_for_add_address_to_user.return_value = expected_output

        actual_output = self.interactor.add_address_to_user(user_id=user_id, address_id=address_id)

        assert actual_output == expected_output

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        self.storage.check_if_address_already_added_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        self.storage.add_address_to_user.assert_called_once_with(user_id=user_id, address_id=address_id)
        self.presenter.get_response_for_add_address_to_user.assert_called_once_with(useraddress_id=useraddress_id)