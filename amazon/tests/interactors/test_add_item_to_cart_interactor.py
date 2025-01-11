from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemDoesNotExistException, CartDoesNotExistException, \
    ItemPropertyDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
import pytest

class TestAddItemToCartInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_item_does_not_exist_raises_exception(self):
        
        item_id = 1
        cart_id = 1
        item_properties = [1, 2]
        item_warranty_id = None
        item_exchange_property_ids = None

        self.storage.check_if_item_exists.side_effect = ItemDoesNotExistException
        self.presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(item_id=item_id, cart_id=cart_id, item_properties=item_properties, \
                                        item_warranty_id=item_warranty_id, item_exchange_property_ids=item_exchange_property_ids)
            
        self.storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.presenter.raise_exception_for_item_does_not_exist.assert_called_once()

    def test_if_cart_does_not_exist_raises_exception(self):

        item_id = 1
        cart_id = 1
        item_properties = [1, 2]
        item_warranty_id = None
        item_exchange_property_ids = None

        self.storage.check_if_cart_exists.side_effect = CartDoesNotExistException
        self.presenter.raise_exception_for_cart_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(item_id=item_id, cart_id=cart_id, item_properties=item_properties, \
                                        item_warranty_id=item_warranty_id, item_exchange_property_ids=item_exchange_property_ids)
            
        self.storage.check_if_cart_exists.assert_called_once_with(cart_id=cart_id)
        self.presenter.raise_exception_for_cart_does_not_exist.assert_called_once()

    def test_if_item_properties_does_not_exist_raises_exception(self):

        item_id = 1
        cart_id = 1
        item_properties = [1, 2]
        item_warranty_id = None
        item_exchange_property_ids = None

        self.storage.check_if_item_properties_exists.side_effect = ItemPropertyDoesNotExistException
        self.presenter.raise_exception_for_item_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(item_id=item_id, cart_id=cart_id, item_properties=item_properties, \
                                        item_warranty_id=item_warranty_id, item_exchange_property_ids=item_exchange_property_ids)
            
        self.storage.check_if_item_properties_exists.assert_called_once_with(item_properties=item_properties)
        self.presenter.raise_exception_for_item_property_does_not_exist.assert_called_once()

    def test_add_item_to_cart(self):

        item_id = 1
        cart_id = 1
        item_properties = [1, 2]
        item_warranty_id = None
        item_exchange_property_ids = None

        self.storage.add_item_to_cart.return_value = None
        self.presenter.get_response_for_add_item_to_cart.return_value = None

        self.interactor.add_item_to_cart(item_id=item_id, cart_id=cart_id, item_properties=item_properties, \
                                        item_warranty_id=item_warranty_id, item_exchange_property_ids=item_exchange_property_ids)
        
        self.storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.storage.check_if_cart_exists.assert_called_once_with(cart_id=cart_id)
        self.storage.check_if_item_properties_exists.assert_called_once_with(item_properties=item_properties)
        self.storage.add_item_to_cart.assert_called_once_with(item_id=item_id, cart_id=cart_id, item_properties=item_properties, \
                                        item_warranty_id=item_warranty_id, item_exchange_property_ids=item_exchange_property_ids)
        self.presenter.get_response_for_add_item_to_cart.assert_called_once()