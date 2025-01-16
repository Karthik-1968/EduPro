from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import CardPaymentMethodDTO, NetBankingPaymentMethodDTO, OrderPaymentDTO, RefundDTO

class PaymentStorageInterface:

    @abstractmethod
    def check_if_card_payment_method_already_exists(self, cardpaymentmethod_dto:CardPaymentMethodDTO):
        pass

    @abstractmethod
    def check_if_net_banking_payment_method_already_exists(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO):
        pass

    @abstractmethod
    def check_if_upi_payment_method_already_exists(self, payment_type:str, upi_id:str):
        pass

    @abstractmethod
    def check_if_cash_on_delivery_payment_method_already_exists(self, payment_type:str):
        pass

    @abstractmethod
    def create_card_payment_method(self, cardpaymentmethod_dto:CardPaymentMethodDTO)->int:
        pass

    @abstractmethod
    def create_net_banking_payment_method(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO)->int:
        pass

    @abstractmethod
    def create_upi_payment_method(self, payment_type:str, upi_id:str)->int:
        pass

    @abstractmethod
    def create_cash_on_delivery_payment_method(self, payment_type:str)->int:
        pass

    @abstractmethod
    def check_if_payment_method_exists(self, paymentmethod_id:int):
        pass

    @abstractmethod
    def add_payment_method_to_order(self, orderpayment_dto:OrderPaymentDTO)->int:
        pass

    @abstractmethod
    def create_refund_request(self, refund_dto:RefundDTO)->int:
        pass

    @abstractmethod
    def check_if_refund_exists(self, refund_id:int):
        pass

    @abstractmethod
    def update_refund_status_after_refunded(self, refund_id:int):
        pass