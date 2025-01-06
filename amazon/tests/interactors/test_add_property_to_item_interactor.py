from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemDoesNotExist, PropertyDoesNotExist, PropertyAlreadyAddedToItem
from mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.item_interactor import ItemInteractor
import pytest

class TestAddPropertyToItemInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_item_does_not_exist_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        self.storage.check_if_item_exists.side_effect = ItemDoesNotExist
        self.presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        self.storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.presenter.raise_exception_for_item_does_not_exist.assert_called_once()

    def test_if_property_does_not_exist_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        self.storage.check_if_property_exists.side_effect = PropertyDoesNotExist
        self.presenter.raise_exception_for_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        self.storage.check_if_property_exists.assert_called_once_with(property_id=property_id)
        self.presenter.raise_exception_for_property_does_not_exist.assert_called_once()

    def test_if_property_already_added_to_item_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        self.storage.check_if_property_already_added_to_item.side_effect = PropertyAlreadyAddedToItem
        self.presenter.raise_exception_for_property_already_added_to_item.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        self.storage.check_if_property_already_added_to_item.assert_called_once_with(item_id=item_id, property_id=property_id,\
         value=value)
        self.presenter.raise_exception_for_property_already_added_to_item.assert_called_once()

    def test_add_property_to_item(self):

        item_id = 1
        property_id = 1
        value =  "value"

        itemproperty_id = 1
        expected_output = {
            "itemproperty_id": itemproperty_id
        }

        self.storage.add_property_to_item.return_value = itemproperty_id
        self.presenter.get_response_for_add_property_to_item.return_value = expected_output

        actual_output = self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        assert actual_output == expected_output

        self.storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.storage.check_if_property_exists.assert_called_once_with(property_id=property_id)
        self.storage.check_if_property_already_added_to_item.assert_called_once_with(item_id=item_id, property_id=property_id, \
        value=value)
        self.storage.add_property_to_item.assert_called_once_with(item_id=item_id, property_id=property_id, value=value)
        self.presenter.get_response_for_add_property_to_item.assert_called_once_with(itemproperty_id=itemproperty_id)