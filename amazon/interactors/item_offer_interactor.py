from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import OfferAlreadyExistsException, ExchangePropertyAlreadyExistsException,\
    ExchangeValueAlreadyExistsException, ExchangeValueDoesNotExistException, ExchangePropertyDoesNotExistException, \
        ItemDoesNotExistException
from typing import Optional
from amazon.interactors.storage_interfaces.storage_interface import OfferDTO

class ItemOfferInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter


    def create_bank_offer(self, offer_type:str, offer_name:Optional[str], card_name:str, discount_in_rupees:int, \
                          discount_in_percentage:float, minimum_purchase_value:Optional[float], minimum_months_emi:Optional[int], \
                          start_date:str, end_date:str, terms_and_conditions:str):
        
        """ELP
            -check if offer already exists
            -create bank offer
        """
        offer_dto = OfferDTO(offer_type=offer_type, offer_name=offer_name, card_name=card_name, discount_in_rupees=discount_in_rupees,\
                             discount_in_percentage=discount_in_percentage, minimum_purchase_value=minimum_purchase_value, minimum_months_emi=minimum_months_emi,\
                             start_date=start_date, end_date=end_date, terms_and_conditions=terms_and_conditions)
        
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except OfferAlreadyExistsException:
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
        except OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_no_cost_emi_offer(offer_type=offer_type)

        return self.presenter.get_response_for_create_no_cost_emi_offer(offer_id=offer_id)
    

    def create_coupon_offer(self, offer_type:str, offer_name:Optional[str], coupon_code:str, discount_in_rupees:int, discount_in_percentage:float, \
                            minimum_purchase_value:Optional[float], start_date:str, end_date:str, terms_and_conditions:str):

        """ELP
            -check if offer already exists
            -create offer
        """

        offer_dto = OfferDTO(offer_type=offer_type, offer_name=offer_name, coupon_code=coupon_code, discount_in_rupees=discount_in_rupees,\
                             discount_in_percentage=discount_in_percentage, minimum_purchase_value=minimum_purchase_value, start_date=start_date,\
                             end_date=end_date, terms_and_conditions=terms_and_conditions)
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except OfferAlreadyExistsException:
            self.presenter.raise_exception_for_offer_already_exists()

        offer_id = self.storage.create_coupon_offer(offer_dto=offer_dto)

        return self.presenter.get_response_for_create_coupon_offer(offer_id=offer_id)
    

    def create_partner_offer(self, offer_type:str, offer_name:Optional[str], minimum_number_of_items:int, discount_in_rupees:int, \
                             discount_in_percentage:float, minimum_purchase_value:Optional[float], start_date:str, end_date:str,\
                                  terms_and_conditions:str):

        """ELP
            -check if offer already exists
            -create offer
        """

        offer_dto = OfferDTO(offer_type=offer_type, offer_name=offer_name, minimum_number_of_items=minimum_number_of_items, \
                             discount_in_rupees=discount_in_rupees, discount_in_percentage=discount_in_percentage, \
                                minimum_purchase_value=minimum_purchase_value, start_date=start_date, end_date=end_date, \
                                    terms_and_conditions=terms_and_conditions)
        try:
            self.storage.check_if_offer_already_exists(offer_dto=offer_dto)
        except OfferAlreadyExistsException:
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
        except ExchangePropertyAlreadyExistsException:
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
        except ExchangeValueAlreadyExistsException:
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
        except ExchangeValueDoesNotExistException:
            self.presenter.raise_exception_for_exchange_value_does_not_exist()

        try:
            self.storage.check_if_exchange_properties_exists(exchange_property_ids=exchange_property_ids)
        except ExchangePropertyDoesNotExistException:
            self.presenter.raise_exception_for_exchange_property_does_not_exist()
        
        self.storage.add_exchange_properties_to_exchange_value(exchange_value_id=exchange_value_id, exchange_property_ids=exchange_property_ids)

        return self.presenter.get_response_for_add_exchange_properties_to_exchange_value()
    

    def add_exchange_properties_to_item(self, item_id:int, exchange_property_ids:list[int]):

        """ELP
            -check if item exists
            -check if all exchange properties exists
            -add properties to item
        """

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_exchange_properties_exists(exchange_property_ids=exchange_property_ids)
        except ExchangePropertyDoesNotExistException:
            self.presenter.raise_exception_for_exchange_property_does_not_exist()
        
        self.storage.add_exchange_properties_to_item(item_id=item_id, exchange_property_ids=exchange_property_ids)

        return self.presenter.get_response_for_add_exchange_properties_to_item()