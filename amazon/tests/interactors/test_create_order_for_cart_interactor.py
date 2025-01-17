from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.exceptions import custom_exceptions
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.storage_interfaces.dtos import OrderCartItemsDTO
from amazon.interactors.order_interactor import OrderInteractor
from mock import create_autospec
import pytest 

class TestCreateOrderForCartInteractor:

    def setup_method(self):
        
        self.user_storage = create_autospec(UserStorageInterface)
        self.order_storage = create_autospec(OrderStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = OrderInteractor(user_storage=self.user_storage, order_storage=self.order_storage, item_storage=self.item_storage)

    def test_if_user_does_not_exist_raises_exception(self):
        
        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12", 
                                          item_ids=[1 ,2, 3],
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.user_storage.check_if_user_exists.side_effect = custom_exceptions.UserDoesNotExistException
        user_presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=ordercartitems_dto.user_id)
        user_presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_cart_does_not_exist_raises_exception(self):

        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12",
                                          item_ids=[1, 2, 3],
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_cart_exists.side_effect = custom_exceptions.CartDoesNotExistException
        item_presenter.raise_exception_for_cart_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_cart_exists.assert_called_once_with(cart_id=ordercartitems_dto.cart_id)
        item_presenter.raise_exception_for_cart_does_not_exist.assert_called_once()

    def test_if_address_does_not_exist_raises_exception(self):

        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12",
                                          item_ids=[1, 2, 3], 
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.user_storage.check_if_address_exists.side_effect = custom_exceptions.AddressDoesNotExistException
        user_presenter.raise_exception_for_address_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.user_storage.check_if_address_exists.assert_called_once_with(address_id=ordercartitems_dto.address_id)
        user_presenter.raise_exception_for_address_does_not_exist.assert_called_once()

    def test_if_test_if_item_does_not_exist_raises_exception(self):

        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12",
                                          item_ids=[1, 2, 3], 
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_items_exists.side_effect = custom_exceptions.ItemDoesNotExistException
        item_presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_items_exists.assert_called_once_with(item_ids=ordercartitems_dto.item_ids)
        item_presenter.raise_exception_for_item_does_not_exist.assert_called_once()


    def test_if_items_do_not_belong_to_cart_raises_exception(self):

        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12", 
                                          item_ids=[1, 2, 3],
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_items_are_in_cart.side_effect = custom_exceptions.ItemDoesNotBelongToCartException
        item_presenter.raise_exception_for_item_does_not_belong_to_cart.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_items_are_in_cart.assert_called_once_with(item_ids=ordercartitems_dto.item_ids, \
                                                                             cart_id=ordercartitems_dto.cart_id)
        item_presenter.raise_exception_for_item_does_not_belong_to_cart.assert_called_once()

    def test_create_order_for_cart(self):

        ordercartitems_dto = OrderCartItemsDTO(user_id="550e8400-e29b-41d4-a716-446655440000", 
                                          cart_id=1, 
                                          address_id=1, 
                                          order_status="ORDERED",
                                          delivery_date="2020-12-12", 
                                          item_ids=[1, 2, 3],
                                          delivery_charges=None, 
                                          receiving_person_name=None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        order_id = 1
        expected_output = {"order_id": order_id}

        self.order_storage.create_order_for_cart.return_value = order_id
        order_presenter.get_response_for_create_order_for_cart.return_value = expected_output

        actual_output = self.interactor.create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        assert actual_output == expected_output

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=ordercartitems_dto.user_id)
        self.item_storage.check_if_cart_exists.assert_called_once_with(cart_id=ordercartitems_dto.cart_id)
        self.user_storage.check_if_address_exists.assert_called_once_with(address_id=ordercartitems_dto.address_id)
        self.item_storage.check_if_items_exists.assert_called_once_with(item_ids=ordercartitems_dto.item_ids)
        self.item_storage.check_if_items_are_in_cart.assert_called_once_with(item_ids=ordercartitems_dto.item_ids, \
                                                                             cart_id=ordercartitems_dto.cart_id)
        self.order_storage.create_order_for_cart.assert_called_once_with(ordercartitems_dto=ordercartitems_dto)
        order_presenter.get_response_for_create_order_for_cart.assert_called_once_with(order_id=order_id)
