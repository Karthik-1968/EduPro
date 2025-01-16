from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.exceptions import custom_exceptions
from mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
import pytest

class TestAddPropertyToItemInteractor:

    def setup_method(self):

        self.item_storage = create_autospec(ItemStorageInterface)
        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.interactor = ItemInteractor(item_storage=self.item_storage, user_storage=self.user_storage, \
                                         category_storage=self.category_storage)

    def test_if_item_does_not_exist_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_item_exists.side_effect = custom_exceptions.ItemDoesNotExistException
        item_presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value, item_presenter=item_presenter)

        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        item_presenter.raise_exception_for_item_does_not_exist.assert_called_once()

    def test_if_property_does_not_exist_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_property_exists.side_effect = custom_exceptions.PropertyDoesNotExistException
        item_presenter.raise_exception_for_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value, item_presenter=item_presenter)

        self.item_storage.check_if_property_exists.assert_called_once_with(property_id=property_id)
        item_presenter.raise_exception_for_property_does_not_exist.assert_called_once()

    def test_if_property_already_added_to_item_raise_exception(self):

        item_id = 1
        property_id = 1
        value =  "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_property_already_added_to_item.side_effect = custom_exceptions.PropertyAlreadyAddedToItemException
        item_presenter.raise_exception_for_property_already_added_to_item.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value, item_presenter=item_presenter)

        self.item_storage.check_if_property_already_added_to_item.assert_called_once_with(item_id=item_id, property_id=property_id,\
         value=value)
        item_presenter.raise_exception_for_property_already_added_to_item.assert_called_once()

    def test_add_property_to_item(self):

        item_id = 1
        property_id = 1
        value =  "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        itemproperty_id = 1
        expected_output = {
            "itemproperty_id": itemproperty_id
        }

        self.item_storage.add_property_to_item.return_value = itemproperty_id
        item_presenter.get_response_for_add_property_to_item.return_value = expected_output

        actual_output = self.interactor.add_property_to_item(item_id=item_id, property_id=property_id, value=value, item_presenter=item_presenter)

        assert actual_output == expected_output

        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.item_storage.check_if_property_exists.assert_called_once_with(property_id=property_id)
        self.item_storage.check_if_property_already_added_to_item.assert_called_once_with(item_id=item_id, property_id=property_id, \
        value=value)
        self.item_storage.add_property_to_item.assert_called_once_with(item_id=item_id, property_id=property_id, value=value)
        item_presenter.get_response_for_add_property_to_item.assert_called_once_with(itemproperty_id=itemproperty_id)