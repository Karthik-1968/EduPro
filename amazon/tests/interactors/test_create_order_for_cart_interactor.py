from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExistException, AddressDoesNotExistException, CartDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import OrderDTO
from amazon.interactors.order_interactor import OrderInteractor
from mock import create_autospec
import pytest 

class TestCreateOrderForCartInteractor:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = OrderInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_user_does_not_exist(self):
        
        user_id = "550e8400-e29b-41d4-a716-446655440000"
        cart_id = 1
        address_id = 1
        status = "ORDERED"
        delivery_date = "2020-12-12"
        delivery_charges = None
        receiving_person_name = None

        self.storage.check_if_user_exists.side_effect = UserDoesNotExistException
        self.presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status,\
             delivery_date=delivery_date, delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_cart_does_not_exist(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        cart_id = 1
        address_id = 1
        status = "ORDERED"
        delivery_date = "2020-12-12"
        delivery_charges = None
        receiving_person_name = None

        self.storage.check_if_cart_exists.side_effect = CartDoesNotExistException
        self.presenter.raise_exception_for_cart_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status,\
             delivery_date=delivery_date, delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)

        self.storage.check_if_cart_exists.assert_called_once_with(cart_id=cart_id)
        self.presenter.raise_exception_for_cart_does_not_exist.assert_called_once()

    def test_if_address_does_not_exist(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        cart_id = 1
        address_id = 1
        status = "ORDERED"
        delivery_date = "2020-12-12"
        delivery_charges = None
        receiving_person_name = None

        self.storage.check_if_address_exists.side_effect = AddressDoesNotExistException
        self.presenter.raise_exception_for_address_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status,\
             delivery_date=delivery_date, delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)

        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        self.presenter.raise_exception_for_address_does_not_exist.assert_called_once()

    def test_create_order_for_cart(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"
        cart_id = 1
        address_id = 1
        status = "ORDERED"
        delivery_date = "2020-12-12"
        delivery_charges = None
        receiving_person_name = None

        order_id = 1
        expected_output = {
            "order_id": order_id
        }

        order_dto = OrderDTO(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status,\
             delivery_date=delivery_date, delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)

        self.storage.create_order_for_cart.return_value = order_id
        self.presenter.get_response_for_create_order_for_cart.return_value = expected_output

        actual_output = self.interactor.create_order_for_cart(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status,\
             delivery_date=delivery_date, delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)

        assert expected_output == actual_output

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.storage.check_if_cart_exists.assert_called_once_with(cart_id=cart_id)
        self.storage.check_if_address_exists.assert_called_once_with(address_id=address_id)
        self.storage.create_order_for_cart.assert_called_once_with(order_dto=order_dto)
        self.presenter.get_response_for_create_order_for_cart.assert_called_once_with(order_id=order_id)
