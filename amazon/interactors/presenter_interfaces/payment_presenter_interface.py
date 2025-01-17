from abc import abstractmethod

class PaymentPresenterInterface:

    @abstractmethod
    def raise_exception_for_card_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_net_banking_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_upi_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_cash_on_delivery_payment_method_already_exists(self):
        pass

    @abstractmethod
    def raise_exception_for_payment_method_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_add_payment_method_to_order(self, payment_id:int):
        pass

    @abstractmethod
    def get_response_for_create_card_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def get_response_for_create_net_banking_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def get_response_for_create_upi_payment_method(self, paymentmethod_id:int):
        pass
    
    @abstractmethod
    def get_response_for_create_cash_on_delivery_payment_method(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def get_response_for_create_refund_request(self, refund_id:int):
        pass

    @abstractmethod
    def raise_exception_for_refund_does_not_exist(self):
        pass

    @abstractmethod
    def get_response_for_update_refund_status_after_refunded(self):
        pass

    @abstractmethod
    def get_response_for_create_order_for_item_and_add_payment_method(self, payment_id:int)->dict:
        pass