from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import OrderItemDTO, OrderCartItemsDTO
from typing import Optional

class OrderInteractor:


    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_order_for_item_wrapper(self, orderitem_dto:OrderItemDTO):
        
        try:
            order_id = self.create_order_for_item(orderitem_dto=orderitem_dto)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()
        except custom_exceptions.AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()
        except custom_exceptions.ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()
        except custom_exceptions.ItemPropertyDoesNotBelongToItemException:
            self.presenter.raise_exception_for_item_property_does_not_belong_to_item()
        except custom_exceptions.OutOfStockException:
            self.presenter.raise_exception_for_out_of_stock()
        else:
            return self.presenter.get_response_for_create_order_for_item(order_id=order_id)

    def create_order_for_item(self, orderitem_dto:OrderItemDTO):

        """ELP
            check if user exists
            check if item exists
            check if address exists
            check if properties exists
            check if number of left in stock is greater than zero
            create_order
        """
        self._check_if_input_data_is_correct_for_create_for_item(orderitem_dto = orderitem_dto)

        return self.storage.create_order_for_item(orderitem_dto=orderitem_dto)
    
    def _check_if_input_data_is_correct_for_create_for_item(self,orderitem_dto:OrderItemDTO):

        self.storage.check_if_user_exists(user_id=orderitem_dto.user_id)

        self.storage.check_if_item_exists(item_id=orderitem_dto.item_id)

        self.storage.check_if_address_exists(address_id=orderitem_dto.address_id)

        self.storage.check_if_item_properties_exists(item_properties=orderitem_dto.item_properties)

        self.storage.check_if_item_properties_belong_to_item(item_properties=orderitem_dto.item_properties, item_id=orderitem_dto.item_id)

        self.storage.check_if_number_of_left_in_stock_is_greater_than_zero(item_id=orderitem_dto.item_id)

    def create_order_for_cart(self, ordercartitems_dto:OrderCartItemsDTO):
        
        """ELP
            -check if user exists
            -check if cart exists
            -check if address exists
            -create_order_for_cart
        """
        self._check_if_input_data_is_correct_for_create_order_for_cart(ordercartitems_dto=ordercartitems_dto)

        order_id = self.storage.create_order_for_cart(ordercartitems_dto=ordercartitems_dto)

        return self.presenter.get_response_for_create_order_for_cart(order_id=order_id)
    
    def _check_if_input_data_is_correct_for_create_order_for_cart(self, ordercartitems_dto:OrderCartItemsDTO):

        try:
            self.storage.check_if_user_exists(user_id=ordercartitems_dto.user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=ordercartitems_dto.address_id)
        except custom_exceptions.AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()

        try:
            self.storage.check_if_items_exists(item_ids=ordercartitems_dto.item_ids)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_cart_exists(cart_id=ordercartitems_dto.cart_id)
        except custom_exceptions.CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_items_are_in_cart(item_ids=ordercartitems_dto.item_ids, cart_id=ordercartitems_dto.cart_id)
        except custom_exceptions.ItemDoesNotBelongToCartException:
            self.presenter.raise_exception_for_item_does_not_belong_to_cart()

    def get_orders_of_user(self, user_id:str):

        """ELP
            check if user exists
            get_orders_of_user
        """
        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        orderid_dtos = self.storage.get_orders_of_user(user_id=user_id)

        return self.presenter.get_response_for_get_orders_of_user(orderid_dtos=orderid_dtos)

    
    def get_orders_of_item(self, item_id:int):

        """ELP
            check if item exists
            get_orders_of_item
        """
        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        orderid_dtos = self.storage.get_orders_of_item(item_id=item_id)

        return self.presenter.get_response_for_get_orders_of_item(orderid_dtos=orderid_dtos)

    
    def delete_order(self, order_id:int):

        """ELP
            check if order exists
            delete_order
        """
        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        self.storage.delete_order(order_id=order_id)

        return self.presenter.get_response_for_delete_order()