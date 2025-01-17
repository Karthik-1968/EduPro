from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.storage_interfaces.item_offer_storage_interface import ItemOfferStorageInterface
from amazon.exceptions import user_custom_exceptions, item_custom_exceptions
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from amazon.interactors.item_interactors.items_cart_interactor import ItemsCartInteractor
from mock import create_autospec
import pytest

class TestCreateItemsCartInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.item_offer_storage = create_autospec(ItemOfferStorageInterface)
        self.interactor = ItemsCartInteractor(user_storage=self.user_storage, item_storage=self.item_storage, \
                                              item_offer_storage=self.item_offer_storage)

    def test_if_user_does_not_exist_raises_exception(self):
        
        user_id = 1
        name = "cart"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)

        self.user_storage.check_if_user_exists.side_effect= user_custom_exceptions.UserDoesNotExistException(user_id=user_id)
        user_presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_cart(user_id=user_id, name=name, user_presenter=user_presenter, item_presenter=item_presenter)
            
        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        user_presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_cart_already_created_raises_exception(self):

        user_id = 1
        name = "cart"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.check_if_cart_already_created_for_user.side_effect = item_custom_exceptions.CartAlreadyCreatedException                                   
        item_presenter.raise_exception_for_cart_already_created.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_cart(user_id=user_id, name=name, user_presenter=user_presenter, item_presenter=item_presenter)
            
        self.item_storage.check_if_cart_already_created_for_user.assert_called_once_with(user_id=user_id)
        item_presenter.raise_exception_for_cart_already_created.assert_called_once()

    def test_create_items_cart(self):

        user_id = 1
        name = "cart"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)

        cart_id = 1
        expected_output = {"cart_id": cart_id}

        self.item_storage.create_cart.return_value = cart_id
        item_presenter.get_response_for_create_cart.return_value = expected_output

        actual_output = self.interactor.create_cart(user_id=user_id, name=name, user_presenter=user_presenter, item_presenter=item_presenter)
        
        assert actual_output == expected_output

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.item_storage.check_if_cart_already_created_for_user.assert_called_once_with(user_id=user_id)
        self.item_storage.create_cart.assert_called_once_with(user_id=user_id, name=name)
        item_presenter.get_response_for_create_cart.assert_called_once_with(cart_id=cart_id)