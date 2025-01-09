from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExistException, ItemDoesNotExistException, AddressDoesNotExistException,\
    ItemPropertyDoesNotExistException, OrderDoesNotExistException, OutOfStockException, CartDoesNotExistException,\
        EmiDoesNotExistException, DeliveryAvailabilityDoesNotExistException, DeliveryAvailabilityAlreadyExistsException, \
            OfferDoesNotExistException, ItemExchangePropertyDoesNotExistException, ItemWarrantyDoesNotExistException
from amazon.interactors.storage_interfaces.storage_interface import OrderDTO, OrderPaymentDTO
from typing import Optional
from amazon.interactors.payment_interactor import PaymentInteractor

class OrderInteractor:


    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_order_for_item_wrapper(self, user_id:str, item_id:int, address_id:int, order_status:str, delivery_date:str,\
                                      item_properties:list[int], delivery_charges:Optional[float], receiving_person_name:Optional[str],\
                                          item_warranty_id:Optional[int]):
        
        order_dto = OrderDTO(user_id=user_id, item_id=item_id, address_id=address_id, order_status=order_status, delivery_date=delivery_date,\
                             item_properties=item_properties, delivery_charges=delivery_charges, \
                                receiving_person_name=receiving_person_name, item_warranty_id=item_warranty_id)
        
        try:
            order_id = self.create_order_for_item(order_dto=order_dto)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()
        except AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()
        except OutOfStockException:
            self.presenter.raise_exception_for_out_of_stock()
        except ItemWarrantyDoesNotExistException:
            self.presenter.raise_exception_for_item_warranty_does_not_exist()
        else:
            return self.presenter.get_response_for_create_order_for_item(order_id=order_id)

    def create_order_for_item(self, order_dto:OrderDTO):

        """ELP
            validate_input_details
                -validate user_id
                -validate item_id
                -validate address_id
                -validate status
                -validate delivery_date
                -validate properties
            check if user exists
            check if item exists
            check if address exists
            check if properties exists
            check if number of left in stock is greater than zero
            create_order
        """
        self._validate_input_details_for_create_order_for_item(user_id=order_dto.user_id, item_id=order_dto.item_id,\
                address_id=order_dto.address_id, order_status=order_dto.order_status, delivery_date=order_dto.delivery_date, \
                    properties=order_dto.item_properties)

        self._check_if_input_data_is_correct_for_create_for_item(order_dto = order_dto)

        return self.storage.create_order_for_item(order_dto=order_dto)

    def _validate_input_details_for_create_order_for_item(self, user_id:str, item_id:int, address_id:int, order_status:str, \
                                                          delivery_date:str, properties:list[int]):
        
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        address_id_not_present = not address_id
        if address_id_not_present:
            self.presenter.raise_exception_for_missing_address_id()

        order_status_not_present = not order_status
        if order_status_not_present:
            self.presenter.raise_exception_for_missing_status()

        delivery_date_not_present = not delivery_date
        if delivery_date_not_present:
            self.presenter.raise_exception_for_missing_delivery_date()

        properties_not_present = not properties
        if properties_not_present:
            self.presenter.raise_exception_for_missing_properties()
    
    def _check_if_input_data_is_correct_for_create_for_item(self,order_dto:OrderDTO):

        self.storage.check_if_user_exists(user_id=order_dto.user_id)

        self.storage.check_if_item_exists(item_id=order_dto.item_id)

        self.storage.check_if_address_exists(address_id=order_dto.address_id)

        self.storage.check_if_item_properties_exists(item_properties=order_dto.item_properties)

        self.storage.check_if_number_of_left_in_stock_is_greater_than_zero(item_id=order_dto.item_id)

        if order_dto.item_warranty_id:
            self.storage.check_if_item_warranty_exists(item_warranty_id=order_dto.item_warranty_id)


    def create_order_for_cart(self, user_id:str, cart_id:int, address_id:int, status:str, delivery_date:str,\
                              delivery_charges:Optional[float], receiving_person_name:Optional[str]):
        
        """ELP
            -check if user exists
            -check if cart exists
            -check if address exists
            -create_order_for_cart
        """
        order_dto = OrderDTO(user_id=user_id, cart_id=cart_id, address_id=address_id, status=status, delivery_date=delivery_date,\
                            delivery_charges=delivery_charges, receiving_person_name=receiving_person_name)
        
        self._check_if_input_data_is_correct_for_create_order_for_cart(order_dto=order_dto)

        order_id = self.storage.create_order_for_cart(order_dto=order_dto)

        return self.presenter.get_response_for_create_order_for_cart(order_id=order_id)
    
    def _check_if_input_data_is_correct_for_create_order_for_cart(self, order_dto:OrderDTO):

        try:
            self.storage.check_if_user_exists(user_id=order_dto.user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_cart_exists(cart_id=order_dto.cart_id)
        except CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=order_dto.address_id)
        except AddressDoesNotExistException:
            self.presenter.raise_exception_for_address_does_not_exist()

    def get_orders_of_user(self, user_id:str):

        """ELP
            validate user_id
            check if user exists
            get_orders_of_user
        """
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        order_dtos = self.storage.get_orders_of_user(user_id=user_id)

        return self.presenter.get_response_for_get_orders_of_user(order_dtos=order_dtos)

    
    def get_orders_of_item(self, item_id:int):

        """ELP
            validate item_id
            check if item exists
            get_orders_of_item
        """
        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        order_dtos = self.storage.get_orders_of_item(item_id=item_id)

        return self.presenter.get_response_for_get_orders_of_item(order_dtos=order_dtos)

    
    def delete_order(self, order_id:int):

        """ELP
            validate order_id
            check if order exists
            delete_order
        """
        order_id_not_present = not order_id
        if order_id_not_present:
            self.presenter.raise_exception_for_missing_order_id()

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        self.storage.delete_order(order_id=order_id)

        return self.presenter.get_response_for_delete_order()
    

    def add_emi_to_order(self, order_id:int, emi_id:int):

        """ELP
            -check if order exists
            -check if emi exists
            -add emi to order
        """

        self._check_if_input_data_is_correct_for_add_emi_to_order(order_id=order_id, emi_id=emi_id)

        self.storage.add_emi_to_order(order_id=order_id, emi_id=emi_id)

        return self.presenter.get_response_for_add_emi_to_order()
    
    def _check_if_input_data_is_correct_for_add_emi_to_order(self, order_id:int, emi_id:int):

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_emi_exists(emi_id=emi_id)
        except EmiDoesNotExistException:
            self.presenter.raise_exception_for_emi_does_not_exist()

    
    def create_delivery_availability(self, can_receive_on_saturday:str, can_receive_on_sunday:str):

        """ELP
            -check if delivery availability exists
            -create delivery aviailability
        """

        try:
            self.storage.check_if_delivery_availability_already_exists(can_receive_on_saturday=can_receive_on_saturday,\
                                                                can_receive__on_sunday=can_receive_on_sunday)
        except DeliveryAvailabilityAlreadyExistsException:
            self.presenter.raise_exception_for_delivery_availability_already_exists()
        
        delivery_availability_id = self.storage.create_delivery_availability(can_receive_on_saturday=can_receive_on_saturday,\
                                                                            can_receive__on_sunday=can_receive_on_sunday)

        return self.presenter.get_response_for_create_delivery_availability(delivery_availability_id=delivery_availability_id)
    

    def add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int):

        """ELP
            -check if order exists
            -check if delivery availability exists
            -add delivery availability to order
        """

        self._check_if_input_data_is_correct_for_add_delivery_availability_to_order(order_id=order_id, \
                                                                            delivery_availability_id=delivery_availability_id)

        self.storage.add_delivery_availability_to_order(order_id=order_id, delivery_availability_id=delivery_availability_id)

        return self.presenter.get_response_for_add_delivery_availability_to_order()
    
    def _check_if_input_data_is_correct_for_add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int):

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_delivery_availability_exists(delivery_availability_id=delivery_availability_id)
        except DeliveryAvailabilityDoesNotExistException:
            self.presenter.raise_exception_for_delivery_availability_does_not_exist()

    
    def add_offer_to_order(self, order_id:int, offer_id:int):

        """ELP
            -check if order exists
            -check if offers exists
            -add offers to order
        """

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_offer_exists(offer_id=offer_id)
        except OfferDoesNotExistException:
            self.presenter.raise_exception_for_offer_does_not_exist()

        self.storage.add_offer_to_order(order_id=order_id, offer_id=offer_id)

        return self.presenter.get_response_for_add_offer_to_order()
    

    def add_item_exchange_properties_to_order(self, order_id:int, item_exchange_property_ids:list[int]):

        """ELP
            -check if order exists
            -check if all exchange properties exists
            -add properties to order
        """

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_item_exchange_properties_exists(item_exchange_property_ids=item_exchange_property_ids)
        except ItemExchangePropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_exchange_property_does_not_exist()

        self.storage.add_item_exchange_properties_to_order(order_id=order_id, item_exchange_property_ids=item_exchange_property_ids)

        return self.presenter.get_response_for_add_item_exchange_properties_to_order()
    

    def create_complete_order_for_item(self, user_id:str, item_id:int, order_status:str, delivery_date:str,\
                                        item_properties:list[int], delivery_charges:Optional[float], receiving_person_name:Optional[str],\
                                            item_warranty_id:Optional[int], payment_method_id:int, payment_status:str,\
                                                amount:float, transaction_id:int, gift_card_or_promo_code:str):

        order_dto = OrderDTO(user_id=user_id, item_id=item_id, order_status=order_status,\
                             delivery_date=delivery_date, item_properties=item_properties, delivery_charges=delivery_charges,\
                                receiving_person_name=receiving_person_name, item_warranty_id=item_warranty_id)
        
        order_id = self.create_order_for_item(order_dto=order_dto)

        orderpayment_dto = OrderPaymentDTO(order_id=order_id, payment_method_id=payment_method_id, payment_status=payment_status,\
                amount=amount, transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)

        payment_id = PaymentInteractor.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)

        return payment_id