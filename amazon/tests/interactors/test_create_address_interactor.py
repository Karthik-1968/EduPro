from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import AddressAlreadyExists
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.user_interactor import UserInteractor
from mock import create_autospec
import pytest

class TestCreateAddressInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = UserInteractor(storage = self.storage, presenter = self.presenter)

    def test_if_address_already_exists_raises_exception(self):

        door_no = "1-1-1"
        street = "vegi vare street"
        city = "hyderabad"
        district = "rangareddy"
        state = "telangana"
        country = "india"
        pincode = "500001"
        contact_number = "9876543210"
        address_type = "home"

        self.storage.check_if_address_already_exists.side_effect = AddressAlreadyExists
        self.presenter.raise_exception_for_address_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_address(door_no=door_no, street=street, city=city, district=district, state=state, \
            country=country, pincode=pincode, contact_number=contact_number, address_type=address_type)
        
        self.storage.check_if_address_already_exists.assert_called_once_with(door_no=door_no, street=street, city=city, \
        district=district, state=state, country=country, pincode=pincode)
        self.presenter.raise_exception_for_address_already_exists.assert_called_once()

    def test_create_address(self):

        door_no = "1-1-1"
        street = "vegi vare street"
        city = "hyderabad"
        district = "rangareddy"
        state = "telangana"
        country = "india"
        pincode = "500001"
        contact_number = "9876543210"
        address_type = "home"

        expected_output = {"address_id":1}

        self.storage.create_address.return_value = 1
        self.presenter.get_response_for_create_address.return_value = expected_output

        actual_output = self.interactor.create_address(door_no=door_no, street=street, city=city, district=district, state=state, \
        country=country, pincode=pincode, contact_number=contact_number, address_type=address_type)

        assert actual_output == expected_output

        self.storage.check_if_address_already_exists.assert_called_once_with(door_no=door_no, street=street, city=city, \
        district=district, state=state, country=country, pincode=pincode)

        self.storage.create_address.assert_called_once_with(door_no=door_no, street=street, city=city, district=district, \
        state=state, country=country, pincode=pincode, contact_number=contact_number, address_type=address_type)
        
        self.presenter.get_response_for_create_address.assert_called_once_with(address_id=1)
