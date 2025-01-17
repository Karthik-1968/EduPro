from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.exceptions import user_custom_exceptions, item_custom_exceptions
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.storage_interfaces.dtos import OrderItemDTO
from amazon.interactors.order_interactor import OrderInteractor
from mock import create_autospec
import pytest 

class TestCreateOrderForItemInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.order_storage = create_autospec(OrderStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = OrderInteractor(user_storage=self.user_storage, order_storage=self.order_storage, item_storage=self.item_storage)

    def test_if_user_does_not_exist_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.user_storage.check_if_user_exists.side_effect = user_custom_exceptions.UserDoesNotExistException(user_id=orderitem_dto.user_id)
        user_presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=orderitem_dto.user_id)
        user_presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_if_item_does_not_exist_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_item_exists.side_effect = item_custom_exceptions.ItemDoesNotExistException(item_id=orderitem_dto.item_id)
        item_presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=orderitem_dto.item_id)
        item_presenter.raise_exception_for_item_does_not_exist.assert_called_once()


    def test_if_address_does_not_exist_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.user_storage.check_if_address_exists.side_effect = user_custom_exceptions.AddressDoesNotExistException(address_id=orderitem_dto.address_id)
        user_presenter.raise_exception_for_address_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.user_storage.check_if_address_exists.assert_called_once_with(address_id=orderitem_dto.address_id)
        user_presenter.raise_exception_for_address_does_not_exist.assert_called_once()


    def check_if_item_properties_does_not_exist_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_item_properties_exists.side_effect = item_custom_exceptions.ItemPropertyDoesNotExistException(\
                                                                            item_property_id=orderitem_dto.item_properties[0])
        item_presenter.raise_exception_for_item_properties_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_item_properties_exists.assert_called_once_with(item_properties=orderitem_dto.properties)
        item_presenter.raise_exception_for_item_properties_does_not_exist.assert_called_once()

    
    def test_if_item_properties_does_not_belong_to_item_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_item_properties_belong_to_item.side_effect = item_custom_exceptions.ItemPropertyDoesNotBelongToItemException(\
                                                    item_property_id=orderitem_dto.item_properties[0], item_id=orderitem_dto.item_id)
        item_presenter.raise_exception_for_item_property_does_not_belong_to_item.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_item_properties_belong_to_item.assert_called_once_with(item_properties=orderitem_dto.item_properties, \
                                                                                          item_id=orderitem_dto.item_id)
        item_presenter.raise_exception_for_item_property_does_not_belong_to_item.assert_called_once()

    
    def test_if_item_is_out_of_stock_raises_exception(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.side_effect = item_custom_exceptions.OutOfStockException
        item_presenter.raise_exception_for_out_of_stock.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.assert_called_once_with(item_id=orderitem_dto.item_id)
        item_presenter.raise_exception_for_out_of_stock.assert_called_once()
    
    def test_create_order(self):

        orderitem_dto = OrderItemDTO(
                            user_id = "550e8400-e29b-41d4-a716-446655440000",
                            item_id = 1,
                            address_id = 1,
                            order_status = "ORDERED",
                            delivery_date = "2020-12-12",
                            item_properties = [1, 2],
                            delivery_charges = None,
                            receiving_person_name = None)
        
        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        order_id = 1
        expected_output = {
            "order_id": order_id
        }

        self.order_storage.create_order_for_item.return_value = order_id
        order_presenter.get_response_for_create_order_for_item.return_value = expected_output

        actual_output = self.interactor.create_order_for_item_wrapper(orderitem_dto=orderitem_dto, user_presenter=user_presenter, item_presenter=\
                                                  item_presenter, order_presenter=order_presenter)

        assert actual_output == expected_output

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=orderitem_dto.user_id)
        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=orderitem_dto.item_id)
        self.user_storage.check_if_address_exists.assert_called_once_with(address_id=orderitem_dto.address_id)
        self.item_storage.check_if_item_properties_exists.assert_called_once_with(item_properties=orderitem_dto.item_properties)
        self.item_storage.check_if_item_properties_belong_to_item.assert_called_once_with(item_properties=orderitem_dto.item_properties, \
                                                                                          item_id=orderitem_dto.item_id)
        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.assert_called_once_with(item_id=orderitem_dto.item_id)
        self.order_storage.create_order_for_item.assert_called_once_with(orderitem_dto=orderitem_dto)
        order_presenter.get_response_for_create_order_for_item.assert_called_once()