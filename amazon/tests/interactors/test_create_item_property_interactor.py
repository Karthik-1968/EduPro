from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PropertyAlreadyExists 
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
from django.core.exceptions import BadRequest
import pytest

class TestCreatePropertyInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_property_already_exists_raise_exception(self):

        property_name = "property1"

        self.storage.check_if_property_already_exists.side_effect = PropertyAlreadyExists
        self.presenter.raise_exception_for_property_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_property(property_name=property_name)

        self.storage.check_if_property_already_exists.assert_called_once_with(property_name=property_name)
        self.presenter.raise_exception_for_property_already_exists.assert_called_once()

    def test_create_property(self):

        property_name = "property1"

        property_id = 1

        expected_output = {
            "property_id": property_id
        }

        self.storage.create_property.return_value = property_id
        self.presenter.get_response_for_create_property.return_value = expected_output

        actual_output = self.interactor.create_property(property_name=property_name)

        assert actual_output == expected_output

        self.storage.check_if_property_already_exists.assert_called_once_with(property_name=property_name)  
        self.storage.create_property.assert_called_once_with(property_name=property_name)
        self.presenter.get_response_for_create_property.assert_called_once_with(property_id=property_id)