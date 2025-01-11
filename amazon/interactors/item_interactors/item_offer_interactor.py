from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from typing import Optional
from amazon.interactors.storage_interfaces.dtos import OfferDTO

class ItemOfferInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter


    def create_bank_offer(self, offer_dto:OfferDTO):
        
        """ELP
            -check if offer already exists
            -create bank offer
        """
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_bank_offer(offer_dto=offer_dto)

        return self.presenter.get_response_for_create_bank_offer(offer_id=offer_id)
    

    def create_no_cost_emi_offer(self, offer_type:str):

        """ELP
            -check if offer already exists
            -create no cost emi offer
        """

        try:
            self.storage.check_if_offer_already_exists(offer_type=offer_type)
        except custom_exceptions.OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_no_cost_emi_offer(offer_type=offer_type)

        return self.presenter.get_response_for_create_no_cost_emi_offer(offer_id=offer_id)
    

    def create_coupon_offer(self, offer_dto:OfferDTO):

        """ELP
            -check if offer already exists
            -create offer
        """
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_coupon_offer(offer_dto=offer_dto)

        return self.presenter.get_response_for_create_coupon_offer(offer_id=offer_id)
    

    def create_partner_offer(self, offer_dto:OfferDTO):

        """ELP
            -check if offer already exists
            -create offer
        """
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except custom_exceptions.OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_partner_offer(offer_dto=offer_dto)

        return self.presenter.get_response_for_create_partner_offer(offer_id=offer_id)
    

    def create_exchange_property(self, property_name:str, property_value:str):

        """ELP
            -check if property already exists
            -create property
        """

        try:
            self.storage.check_if_exchange_property_already_exists(property_name=property_name, property_value=property_value)
        except custom_exceptions.ExchangePropertyAlreadyExistsException:
            self.presenter.raise_exception_for_exchange_property_already_exists()

        exchange_property_id = self.storage.create_exchange_property(property_name=property_name, property_value=property_value)

        return self.presenter.get_response_for_create_exchange_property(exchange_property_id=exchange_property_id)
    
    def create_exchange_value(self, exchange_discount:float, service_charge:float):
        
        """ELP
            -check if exchange value already exists
            -create exchange value
        """

        try:
            self.storage.check_if_exchange_value_already_exists(exchange_discount=exchange_discount, service_charge=service_charge)
        except custom_exceptions.ExchangeValueAlreadyExistsException:
            self.presenter.raise_exception_for_exchange_value_already_exists()

        exchange_value_id = self.storage.create_exchange_value(exchange_discount=exchange_discount, service_charge=service_charge)

        return self.presenter.get_response_for_create_exchange_value(exchange_value_id=exchange_value_id)
    

    def add_exchange_properties_to_exchange_value(self, exchange_value_id:int, exchange_property_ids:list[int]):

        """ELP
            -check if exchange value exists
            -check if all exchange properties exists
            -add properties to exchange value
        """

        try:
            self.storage.check_if_exchange_value_exists(exchange_value_id=exchange_value_id)
        except custom_exceptions.ExchangeValueDoesNotExistException:
            self.presenter.raise_exception_for_exchange_value_does_not_exist()

        try:
            self.storage.check_if_exchange_properties_exists(exchange_property_ids=exchange_property_ids)
        except custom_exceptions.ExchangePropertyDoesNotExistException:
            self.presenter.raise_exception_for_exchange_property_does_not_exist()
        
        self.storage.add_exchange_properties_to_exchange_value(exchange_value_id=exchange_value_id, \
                                                               exchange_property_ids=exchange_property_ids)

        return self.presenter.get_response_for_add_exchange_properties_to_exchange_value()
    

    def add_exchange_property_to_item(self, item_id:int, exchange_property_id:int):

        """ELP
            -check if item exists
            -check if all exchange properties exists
            -add properties to item
        """

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_exchange_property_exists(exchange_property_id=exchange_property_id)
        except custom_exceptions.ExchangePropertyDoesNotExistException:
            self.presenter.raise_exception_for_exchange_property_does_not_exist()
        
        item_exchange_property_id = self.storage.add_exchange_properties_to_item(item_id=item_id, exchange_property_id=exchange_property_id)

        return self.presenter.get_response_for_add_exchange_properties_to_item(item_exchange_property_id=item_exchange_property_id)
    

    def add_offer_to_item(self, item_id:int, offer_id:int):

        """ELP
            -check if item exists
            -check if offer exists
            -add offer to item
        """
        
        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_offer_exists(offer_id=offer_id)
        except custom_exceptions.OfferDoesNotExistException:
            self.presenter.raise_exception_for_offer_does_not_exist()
        
        item_offer_id = self.storage.add_offer_to_item(item_id=item_id, offer_id=offer_id)

        return self.presenter.get_response_for_add_offer_to_item(item_offer_id=item_offer_id)