from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.exceptions import order_custom_exceptions, item_custom_exceptions, user_custom_exceptions
from amazon.interactors.storage_interfaces.dtos import OrderItemDTO, OrderCartItemsDTO, PaymentDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from typing import Optional

class OrderInteractor:


    def __init__(self, user_storage: UserStorageInterface, order_storage: OrderStorageInterface, item_storage: \
                    ItemStorageInterface, payment_storage: PaymentStorageInterface):
        
        self.user_storage = user_storage
        self.order_storage = order_storage
        self.item_storage = item_storage
        self.payment_storage = payment_storage

    def create_order_for_item_wrapper(self, orderitem_dto:OrderItemDTO, user_presenter:UserPresenterInterface, item_presenter:ItemPresenterInterface,\
                                      order_presenter:OrderPresenterInterface):
        
        try:
            order_id = self.create_order_for_item(orderitem_dto=orderitem_dto)
        except user_custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()
        except item_custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()
        except user_custom_exceptions.AddressDoesNotExistException:
            user_presenter.raise_exception_for_address_does_not_exist()
        except item_custom_exceptions.ItemPropertyDoesNotExistException:
            item_presenter.raise_exception_for_item_property_does_not_exist()
        except item_custom_exceptions.ItemPropertyDoesNotBelongToItemException:
            item_presenter.raise_exception_for_item_property_does_not_belong_to_item()
        except item_custom_exceptions.OutOfStockException:
            item_presenter.raise_exception_for_out_of_stock()
        else:
            return order_presenter.get_response_for_create_order_for_item(order_id=order_id)

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

        return self.order_storage.create_order_for_item(orderitem_dto=orderitem_dto)
    
    def _check_if_input_data_is_correct_for_create_for_item(self,orderitem_dto:OrderItemDTO):

        self.user_storage.check_if_user_exists(user_id=orderitem_dto.user_id)

        self.item_storage.check_if_item_exists(item_id=orderitem_dto.item_id)

        self.user_storage.check_if_address_exists(address_id=orderitem_dto.address_id)

        self.item_storage.check_if_item_properties_exists(item_properties=orderitem_dto.item_properties)

        self.item_storage.check_if_item_properties_belong_to_item(item_properties=orderitem_dto.item_properties, item_id=orderitem_dto.item_id)

        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero(item_id=orderitem_dto.item_id)

    def create_order_for_cart(self, ordercartitems_dto:OrderCartItemsDTO, user_presenter:UserPresenterInterface, \
                              item_presenter:ItemPresenterInterface, order_presenter:OrderPresenterInterface):
        
        """ELP
            -check if user exists
            -check if cart exists
            -check if address exists
            -check if items exists
            -check if items belong to cart
            -create_order_for_cart
        """
        self._check_if_input_data_is_correct_for_create_order_for_cart(ordercartitems_dto=ordercartitems_dto, user_presenter=user_presenter, \
                                                                       item_presenter=item_presenter)

        order_id = self.order_storage.create_order_for_cart(ordercartitems_dto=ordercartitems_dto)

        return order_presenter.get_response_for_create_order_for_cart(order_id=order_id)
    
    def _check_if_input_data_is_correct_for_create_order_for_cart(self, ordercartitems_dto:OrderCartItemsDTO, user_presenter:UserPresenterInterface, \
                                                                  item_presenter:ItemPresenterInterface):

        try:
            self.user_storage.check_if_user_exists(user_id=ordercartitems_dto.user_id)
        except user_custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()

        try:
            self.user_storage.check_if_address_exists(address_id=ordercartitems_dto.address_id)
        except user_custom_exceptions.AddressDoesNotExistException:
            user_presenter.raise_exception_for_address_does_not_exist()

        try:
            self.item_storage.check_if_items_exists(item_ids=ordercartitems_dto.item_ids)
        except item_custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_cart_exists(cart_id=ordercartitems_dto.cart_id)
        except item_custom_exceptions.CartDoesNotExistException:
            item_presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.item_storage.check_if_items_are_in_cart(item_ids=ordercartitems_dto.item_ids, cart_id=ordercartitems_dto.cart_id)
        except item_custom_exceptions.ItemDoesNotExistInCartException:
            item_presenter.raise_exception_for_item_does_not_belong_to_cart()

    def get_orders_of_user(self, user_id:str, user_presenter:UserPresenterInterface, order_presenter:OrderPresenterInterface):

        """ELP
            check if user exists
            get_orders_of_user
        """
        try:
            self.user_storage.check_if_user_exists(user_id=user_id)
        except user_custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()

        orderid_dtos = self.order_storage.get_orders_of_user(user_id=user_id)

        return order_presenter.get_response_for_get_orders_of_user(orderid_dtos=orderid_dtos)

    
    def get_orders_of_item(self, item_id:int, item_presenter:ItemPresenterInterface, order_presenter:OrderPresenterInterface):

        """ELP
            check if item exists
            get_orders_of_item
        """
        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except item_custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()

        orderid_dtos = self.order_storage.get_orders_of_item(item_id=item_id)

        return order_presenter.get_response_for_get_orders_of_item(orderid_dtos=orderid_dtos)

    
    def delete_order(self, order_id:int, order_presenter:OrderPresenterInterface):

        """ELP
            check if order exists
            delete_order
        """
        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except order_custom_exceptions.OrderDoesNotExistException:
            order_presenter.raise_exception_for_order_does_not_exist()

        self.order_storage.delete_order(order_id=order_id)

        return order_presenter.get_response_for_delete_order()


    def create_order_for_item_and_add_payment_method_wrapper(self, orderitem_dto:OrderItemDTO, payment_dto:PaymetDTO, \
                user_presenter:UserPresenterInterface, item_presenter:ItemPresenterInterface, order_presenter:OrderPresenterInterface, \
                                                             payment_presenter:PaymentPresenterInterface):      

        """ELP
            check if paymentmethod exists
            check if user exists
            check if address exists
            check if item exists
            check if properties exists
            check if properties belongs to item
            check if number of left in stock is greater than zero
            create_order
            create_payment
        """
        try:
            payment_id = self.create_order_for_item_and_add_payment_method(orderitem_dto=orderitem_dto, payment_dto=payment_dto)
        except user_custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()
        except item_custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()
        except user_custom_exceptions.AddressDoesNotExistException:
            user_presenter.raise_exception_for_address_does_not_exist()
        except item_custom_exceptions.ItemPropertyDoesNotExistException:
            item_presenter.raise_exception_for_item_property_does_not_exist()
        except item_custom_exceptions.ItemPropertyDoesNotBelongToItemException:
            item_presenter.raise_exception_for_item_property_does_not_belong_to_item()
        except item_custom_exceptions.OutOfStockException:
            item_presenter.raise_exception_for_out_of_stock()
        except payment_custom_exceptions.PaymentMethodDoesNotExistException:
            payment_presenter.raise_exception_for_payment_method_does_not_exist()
        else:
            return payment_presenter.get_response_for_create_order_for_item_and_add_payment_method(payment_id=payment_id)
    
    def create_order_for_item_and_add_payment_method(self, payment_dto:PaymentDTO):

        self._check_if_input_data_is_correct_for_create_for_item(orderitem_dto=orderitem_dto, payment_dto = payment_dto)

        order_id = self.create_order_for_item(orderitem_dto=orderitem_dto)

        orderpayment_dto = OrderPaymentDTO(order_id=order_id, paymentmethod_id=payment_dto.paymentmethod_id, payment_status=\
                            payment_dto.payment_status, transaction_id=payment_dto.transaction_id, amount=payment_dto.amount,\
                            gift_card_or_promo_code=payment_dto.gift_card_or_promo_code)

        payment_interactor = PaymentInteractor(payment_storage=self.payment_storage)

        payment_id = payment_interactor.create_payment(orderpayment_dto=orderpayment_dto)

        return payment_id
    
    def _check_if_input_data_is_correct_for_create_for_item(self, orderitem_dto:OrderItemDTO, payment_dto:PaymentDTO):

        self.payment_storage.check_if_paymentmethod_exists(paymentmethod_id=payment_dto.paymentmethod_id)

        self.user_storage.check_if_user_exists(user_id=orderitem_dto.user_id)

        self.item_storage.check_if_item_exists(item_id=orderitem_dto.item_id)

        self.user_storage.check_if_address_exists(address_id=orderitem_dto.address_id)

        self.item_storage.check_if_item_properties_exists(item_properties=orderitem_dto.item_properties)

        self.item_storage.check_if_item_properties_belong_to_item(item_properties=orderitem_dto.item_properties, item_id=orderitem_dto.item_id)

        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero(item_id=orderitem_dto.item_id)
        