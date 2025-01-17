from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions.user_custom_exceptions import AddressAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.address_interactor import AddressInteractor
from amazon.interactors.storage_interfaces.dtos import AddressDTO
from mock import create_autospec
import pytest

class TestCreateAddressInteractor:

    def setup_method(self):

        self.storage = create_autospec(UserStorageInterface)
        self.interactor = AddressInteractor(storage = self.storage)

    def test_if_address_already_exists_raises_exception(self):

        address_dto = AddressDTO(
        door_no = "1-1-1",
        street = "vegi vare street",
        city = "hyderabad",
        district = "rangareddy",
        state = "telangana",
        country = "india",
        pincode = "500001",
        contact_number = "9876543210",
        address_type = "home")

        presenter = create_autospec(UserPresenterInterface)

        self.storage.check_if_address_already_exists.side_effect = AddressAlreadyExistsException
        presenter.raise_exception_for_address_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_address(address_dto=address_dto, presenter=presenter)
        
        self.storage.check_if_address_already_exists.assert_called_once_with(address_dto=address_dto)
        presenter.raise_exception_for_address_already_exists.assert_called_once()

    def test_create_address(self):

        address_dto = AddressDTO(
        door_no = "1-1-1",
        street = "vegi vare street",
        city = "hyderabad",
        district = "rangareddy",
        state = "telangana",
        country = "india",
        pincode = "500001",
        contact_number = "9876543210",
        address_type = "home")

        presenter = create_autospec(UserPresenterInterface)

        address_id = 1
        expected_output = {"address_id": address_id}

        self.storage.create_address.return_value = address_id
        presenter.get_response_for_create_address.return_value = expected_output

        actual_output = self.interactor.create_address(address_dto=address_dto, presenter=presenter)

        assert actual_output == expected_output

        self.storage.check_if_address_already_exists.assert_called_once_with(address_dto=address_dto)
        self.storage.create_address.assert_called_once_with(address_dto=address_dto)
        presenter.get_response_for_create_address.assert_called_once_with(address_id=address_id)
