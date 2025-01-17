from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.exceptions.custom_exceptions import ItemPropertyDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
import pytest

class TestUpdateItemPropertyInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = ItemInteractor(user_storage=self.user_storage, category_storage=self.category_storage, item_storage=self.item_storage)

    def test_if_item_property_does_not_exist_raises_exception(self):

        item_property_id = 1
        value = "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_item_property_exists.side_effect = ItemPropertyDoesNotExistException
        item_presenter.raise_exception_for_item_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.update_item_property(item_property_id=item_property_id, value=value, item_presenter=item_presenter)
            
        self.item_storage.check_if_item_property_exists.assert_called_once_with(item_property_id=item_property_id)
        item_presenter.raise_exception_for_item_property_does_not_exist.assert_called_once()

    def test_update_item_property(self):

        item_property_id = 1
        value = "value"

        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.update_item_property.return_value = None
        item_presenter.get_response_for_update_item_property.return_value = None

        self.interactor.update_item_property(item_property_id=item_property_id, value=value, item_presenter=item_presenter)

        self.item_storage.check_if_item_property_exists.assert_called_once_with(item_property_id=item_property_id)
        self.item_storage.update_item_property.assert_called_once_with(item_property_id=item_property_id, value=value)
        item_presenter.get_response_for_update_item_property.assert_called_once()