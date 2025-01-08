from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import CartAlreadyCreatedException, UserDoesNotExistException
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from amazon.interactors.item_interactor import ItemInteractor
from mock import create_autospec
import pytest

class TestCreateItemsCartInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_user_does_not_exist_raises_exception(self):
        
        user_id = 1
        name = "cart"

        self.storage.check_if_user_exists.side_effect= UserDoesNotExistException
        self.presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_cart(user_id=user_id, name=name)
            
        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_cart_already_created_raises_exception(self):

        user_id = 1
        name = "cart"

        self.storage.check_if_cart_already_created_for_user.side_effect = CartAlreadyCreatedException
        self.presenter.raise_exception_for_cart_already_created.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_cart(user_id=user_id, name=name)
            
        self.storage.check_if_cart_already_created_for_user.assert_called_once_with(user_id=user_id)
        self.presenter.raise_exception_for_cart_already_created.assert_called_once()

    def test_create_items_cart(self):

        user_id = 1
        name = "cart"

        cart_id = 1
        expected_output = {"cart_id": cart_id}

        self.storage.create_cart.return_value = cart_id
        self.presenter.get_response_for_create_cart.return_value = expected_output

        actual_output = self.interactor.create_cart(user_id=user_id, name=name)
        
        assert actual_output == expected_output

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.storage.check_if_cart_already_created_for_user.assert_called_once_with(user_id=user_id)
        self.storage.create_cart.assert_called_once_with(user_id=user_id, name=name)
        self.presenter.get_response_for_create_cart.assert_called_once_with(cart_id=cart_id)