from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemPropertyDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
import pytest


class TestDeleteItemPropertyInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_item_property_does_not_exist(self):

        item_property_id = 1

        self.storage.check_if_item_property_exists.side_effect = ItemPropertyDoesNotExistException
        self.presenter.raise_exception_for_item_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.delete_item_property(item_property_id=item_property_id)
            
        self.storage.check_if_item_property_exists.assert_called_once_with(item_property_id=item_property_id)
        self.presenter.raise_exception_for_item_property_does_not_exist.assert_called_once()

    def test_delete_item_property(self):

        item_property_id = 1

        self.storage.delete_item_property.return_value = None
        self.presenter.get_response_for_delete_item_property.return_value = None

        self.interactor.delete_item_property(item_property_id=item_property_id)
        
        self.storage.check_if_item_property_exists.assert_called_once_with(item_property_id=item_property_id)
        self.storage.delete_item_property.assert_called_once_with(item_property_id=item_property_id)
        self.presenter.get_response_for_delete_item_property.assert_called_once()