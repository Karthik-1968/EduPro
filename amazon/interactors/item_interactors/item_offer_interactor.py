from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.item_offer_storage_interface import ItemOfferStorageInterface
from amazon.interactors.presenter_interfaces.item_offer_presenter_interface import ItemOfferPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.exceptions import custom_exceptions
from typing import Optional
from amazon.interactors.storage_interfaces.dtos import OfferDTO

class ItemOfferInteractor:

    def __init__(self, item_storage:ItemStorageInterface, item_presenter:ItemPresenterInterface, \
                 item_offer_storage:ItemOfferStorageInterface, item_offer_presenter:ItemOfferPresenterInterface, 
                 order_storage:OrderStorageInterface, order_presenter:OrderPresenterInterface):

        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.item_offer_storage = item_offer_storage
        self.item_offer_presenter = item_offer_presenter
        self.order_storage = order_storage
        self.order_presenter = order_presenter



    def create_bank_offer(self, offer_dto:OfferDTO):
        
        """ELP
            -check if offer already exists
            -create bank offer
        """
        try:
            self.item_offer_storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_offer_already_exists()

        offer_id = self.item_offer_storage.create_bank_offer(offer_dto=offer_dto)

        return self.item_offer_presenter.get_response_for_create_bank_offer(offer_id=offer_id)
    

    def create_no_cost_emi_offer(self, offer_type:str):

        """ELP
            -check if offer already exists
            -create no cost emi offer
        """

        try:
            self.item_offer_storage.check_if_offer_already_exists(offer_type=offer_type)
        except custom_exceptions.OfferAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_offer_already_exists()

        offer_id = self.item_offer_storage.create_no_cost_emi_offer(offer_type=offer_type)

        return self.item_offer_presenter.get_response_for_create_no_cost_emi_offer(offer_id=offer_id)
    

    def create_coupon_offer(self, offer_dto:OfferDTO):

        """ELP
            -check if offer already exists
            -create offer
        """
        try:
            self.item_offer_storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_offer_already_exists()

        offer_id = self.item_offer_storage.create_coupon_offer(offer_dto=offer_dto)

        return self.item_offer_presenter.get_response_for_create_coupon_offer(offer_id=offer_id)
    

    def create_partner_offer(self, offer_dto:OfferDTO):

        """ELP
            -check if offer already exists
            -create offer
        """
        try:
            self.item_offer_storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_offer_already_exists()

        offer_id = self.item_offer_storage.create_partner_offer(offer_dto=offer_dto)

        return self.item_offer_presenter.get_response_for_create_partner_offer(offer_id=offer_id)
    

    def create_exchange_property(self, property_name:str, property_value:str):

        """ELP
            -check if property already exists
            -create property
        """

        try:
            self.item_offer_storage.check_if_exchange_property_already_exists(property_name=property_name, property_value=property_value)
        except custom_exceptions.ExchangePropertyAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_exchange_property_already_exists()

        exchange_property_id = self.item_offer_storage.create_exchange_property(property_name=property_name, property_value=property_value)

        return self.item_offer_presenter.get_response_for_create_exchange_property(exchange_property_id=exchange_property_id)
    
    def create_exchange_value(self, exchange_discount:float, service_charge:float):
        
        """ELP
            -check if exchange value already exists
            -create exchange value
        """

        try:
            self.item_offer_storage.check_if_exchange_value_already_exists(exchange_discount=exchange_discount, service_charge=service_charge)
        except custom_exceptions.ExchangeValueAlreadyExistsException:
            self.item_offer_presenter.raise_exception_for_exchange_value_already_exists()

        exchange_value_id = self.item_offer_storage.create_exchange_value(exchange_discount=exchange_discount, service_charge=service_charge)

        return self.item_offer_presenter.get_response_for_create_exchange_value(exchange_value_id=exchange_value_id)
    

    def add_exchange_properties_to_exchange_value(self, exchange_value_id:int, exchange_property_ids:list[int]):

        """ELP
            -check if exchange value exists
            -check if all exchange properties exists
            -add properties to exchange value
        """

        try:
            self.item_offer_storage.check_if_exchange_value_exists(exchange_value_id=exchange_value_id)
        except custom_exceptions.ExchangeValueDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_exchange_value_does_not_exist()

        try:
            self.item_offer_storage.check_if_exchange_properties_exists(exchange_property_ids=exchange_property_ids)
        except custom_exceptions.ExchangePropertyDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_exchange_property_does_not_exist()
        
        self.item_offer_storage.add_exchange_properties_to_exchange_value(exchange_value_id=exchange_value_id, \
                                                               exchange_property_ids=exchange_property_ids)

        return self.item_offer_presenter.get_response_for_add_exchange_properties_to_exchange_value()
    

    def add_exchange_property_to_item(self, item_id:int, exchange_property_id:int):

        """ELP
            -check if item exists
            -check if all exchange properties exists
            -add properties to item
        """

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_offer_storage.check_if_exchange_property_exists(exchange_property_id=exchange_property_id)
        except custom_exceptions.ExchangePropertyDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_exchange_property_does_not_exist()
        
        item_exchange_property_id = self.item_offer_storage.add_exchange_properties_to_item(item_id=item_id, exchange_property_id=exchange_property_id)

        return self.item_offer_presenter.get_response_for_add_exchange_properties_to_item(item_exchange_property_id=item_exchange_property_id)
    

    def add_offer_to_item(self, item_id:int, offer_id:int):

        """ELP
            -check if item exists
            -check if offer exists
            -add offer to item
        """
        
        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_offer_storage.check_if_offer_exists(offer_id=offer_id)
        except custom_exceptions.OfferDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_offer_does_not_exist()
        
        item_offer_id = self.item_offer_storage.add_offer_to_item(item_id=item_id, offer_id=offer_id)

        return self.item_offer_presenter.get_response_for_add_offer_to_item(item_offer_id=item_offer_id)
    

    def add_offer_to_order(self, order_id:int, offer_id:int):
        
        """ELP
            -check if order exists
            -check if offer exists
            -check if offer is specific to item in order
            -check if offer is already added to order
            -add offer to order
        """
        self._check_if_input_data_is_correct_for_add_offer_to_order(order_id=order_id, offer_id=offer_id)

        self.item_offer_storage.add_offer_to_order(order_id=order_id, offer_id=offer_id)

        return self.item_offer_presenter.get_response_for_add_offer_to_order()
    
    def _check_if_input_data_is_correct_for_add_offer_to_order(self, order_id:int, offer_id:int):

        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.order_presenter.raise_exception_for_order_does_not_exist()
        
        try:
            self.item_offer_storage.check_if_offer_exists(offer_id=offer_id)
        except custom_exceptions.OfferDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_offer_does_not_exist()
        
        try:
            self.item_offer_storage.check_if_offer_is_specific_to_item_in_order(order_id=order_id, offer_id=offer_id)
        except custom_exceptions.OfferIsNotSpecificToItemInOrderException:
            self.item_offer_presenter.raise_exception_for_offer_is_not_specific_to_item_in_order()
        
        try:
            self.item_offer_storage.check_if_offer_is_already_added_to_order(order_id=order_id, offer_id=offer_id)
        except custom_exceptions.OfferAlreadyAddedToOrderException:
            self.item_offer_presenter.raise_exception_for_offer_already_added_to_order()

    
    def add_exchange_properties_to_order(self, order_id:int, exchange_property_ids:list[int]):

        """ELP
            -check if order exists
            -check if all exchange properties exists
            -check if exchange properties are associated with item in order
            -check if exchange properties are already added to order
            -add properties to order
        """

        self._check_if_input_data_is_correct_for_add_exchange_properties_to_order(order_id=order_id, \
                                                                                  exchange_property_ids=exchange_property_ids)
        
        self.item_offer_storage.add_exchange_properties_to_order(order_id=order_id, exchange_property_ids=exchange_property_ids)

        return self.item_offer_presenter.get_response_for_add_exchange_properties_to_order()
        
    def _check_if_input_data_is_correct_for_add_exchange_properties_to_order(self, order_id:int, exchange_property_ids:list[int]):

        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.order_presenter.raise_exception_for_order_does_not_exist()
        
        try:
            self.item_offer_storage.check_if_exchange_properties_exists(exchange_property_ids=exchange_property_ids)
        except custom_exceptions.ExchangePropertyDoesNotExistException:
            self.item_offer_presenter.raise_exception_for_exchange_property_does_not_exist()
        
        try:
            self.item_offer_storage.check_if_exchange_properties_are_associated_with_item_in_order(order_id=order_id, \
                                                                                        exchange_property_ids=exchange_property_ids)
        except custom_exceptions.ExchangePropertiesAreNotAssociatedWithItemInOrderException:
            self.item_offer_presenter.raise_exception_for_exchange_properties_are_not_associated_with_item_in_order()
        
        try:
            self.item_offer_storage.check_if_exchange_properties_are_already_added_to_order(order_id=order_id, \
                                                                                exchange_property_ids=exchange_property_ids)
        except custom_exceptions.ExchangePropertiesAreAlreadyAddedToOrderException:
            self.item_offer_presenter.raise_exception_for_exchange_properties_are_already_added_to_order()