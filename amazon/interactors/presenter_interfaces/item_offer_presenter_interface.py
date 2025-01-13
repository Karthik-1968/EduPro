from abc import abstractmethod

class ItemOfferPresenterInterface:

    @abstractmethod
    def raise_exception_for_offer_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_bank_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_no_cost_emi_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_coupon_offer(self, offer_id:int):
        pass

    @abstractmethod
    def get_response_for_create_partner_offer(self, offer_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_property_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_exchange_property(self, exchange_property_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_value_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_exchange_value(self, exchange_value_id:int):
        pass

    @abstractmethod
    def raise_exception_for_exchange_value_does_not_exist(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_exchange_value(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_item(self, item_exchange_property_id:int):
        pass

    @abstractmethod
    def raise_exception_for_offer_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_offer_to_item(self, item_offer_id:int):
        pass

    @abstractmethod
    def get_response_for_add_offer_to_order(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_item_exchange_property_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_item_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_offer_is_not_specific_to_item_in_order(self):
        pass

    @abstractmethod
    def raise_exception_for_offer_already_added_to_order(self):
        pass

    @abstractmethod
    def get_response_for_add_exchange_properties_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_properties_are_already_added_to_order(self):
        pass

    @abstractmethod
    def raise_exception_for_exchange_properties_are_not_associated_with_item_in_order(self):
        pass