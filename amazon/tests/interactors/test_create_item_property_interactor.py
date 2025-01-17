from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.exceptions.item_custom_exceptions import PropertyAlreadyExistsException
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
from django.core.exceptions import BadRequest
import pytest

class TestCreatePropertyInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = ItemInteractor(user_storage=self.user_storage, category_storage=self.category_storage, item_storage=self.item_storage)

    def test_if_property_already_exists_raises_exception(self):

        property_name = "property1"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_property_already_exists.side_effect = PropertyAlreadyExistsException
        item_presenter.raise_exception_for_property_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_property(property_name=property_name, item_presenter=item_presenter)

        self.item_storage.check_if_property_already_exists.assert_called_once_with(property_name=property_name)
        item_presenter.raise_exception_for_property_already_exists.assert_called_once()

    def test_create_property(self):

        property_name = "property1"

        item_presenter = create_autospec(ItemPresenterInterface)

        property_id = 1
        expected_output = {
            "property_id": property_id
        }

        self.item_storage.create_property.return_value = property_id
        item_presenter.get_response_for_create_property.return_value = expected_output

        actual_output = self.interactor.create_property(property_name=property_name, item_presenter=item_presenter)

        assert actual_output == expected_output

        self.item_storage.check_if_property_already_exists.assert_called_once_with(property_name=property_name)  
        self.item_storage.create_property.assert_called_once_with(property_name=property_name)
        item_presenter.get_response_for_create_property.assert_called_once_with(property_id=property_id)