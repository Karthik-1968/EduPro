from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import CardPaymentMethodDTO, NetBankingPaymentMethodDTO, OrderPaymentDTO
from typing import Optional


class PaymentInteractor():

    def __init__(self, order_storage: OrderStorageInterface, payment_storage: PaymentStorageInterface):
        
        self.order_storage = order_storage
        self.payment_storage = payment_storage


    def create_card_payment_method(self, cardpaymentmethod_dto: CardPaymentMethodDTO, payment_presenter: PaymentPresenterInterface):

        """ELP
            check if payment method already exists
            create payment method
        """
        self._check_if_input_data_is_correct_for_create_card_payment(cardpaymentmethod_dto=cardpaymentmethod_dto, \
                                                                     payment_presenter=payment_presenter)

        paymentmethod_id = self.payment_storage.create_card_payment_method(cardpaymentmethod_dto=cardpaymentmethod_dto)

        return payment_presenter.get_response_for_create_card_payment_method(paymentmethod_id=paymentmethod_id)

    def _check_if_input_data_is_correct_for_create_card_payment(self, cardpaymentmethod_dto:CardPaymentMethodDTO, \
                                                                payment_presenter: PaymentPresenterInterface):
    
        try:
            self.payment_storage.check_if_card_payment_method_already_exists(cardpaymentmethod_dto=cardpaymentmethod_dto)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            payment_presenter.raise_exception_for_card_payment_method_already_exists()


    def create_net_banking_payment_method(self, netbankingpaymentmethod_dto: NetBankingPaymentMethodDTO, \
                                          payment_presenter: PaymentPresenterInterface):

        """ELP
            check if payment method already exists
            create payment method
        """
        self._check_if_input_data_is_correct_for_create_net_banking_payment(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto, \
                                                                            payment_presenter=payment_presenter)

        paymentmethod_id = self.payment_storage.create_net_banking_payment_method(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)

        return payment_presenter.get_response_for_create_net_banking_payment_method(paymentmethod_id=paymentmethod_id)

    def _check_if_input_data_is_correct_for_create_net_banking_payment(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO, \
                                                                       payment_presenter: PaymentPresenterInterface):

        try:
            self.payment_storage.check_if_net_banking_payment_method_already_exists(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            payment_presenter.raise_exception_for_net_banking_payment_method_already_exists()


    def create_upi_payment_method(self, payment_type:str, upi_id:str, payment_presenter: PaymentPresenterInterface):

        """ELP
            check if payment method already exists
            create payment method
        """
        self._check_if_input_data_is_correct_for_create_upi_payment(payment_type=payment_type, upi_id=upi_id, \
                                                                    payment_presenter=payment_presenter)

        paymentmethod_id = self.payment_storage.create_upi_payment_method(payment_type=payment_type, upi_id=upi_id)

        return self.payment_presenter.get_response_for_create_upi_payment_method(paymentmethod_id=paymentmethod_id)

    def _check_if_input_data_is_correct_for_create_upi_payment(self, payment_type:str, upi_id:str, payment_presenter: PaymentPresenterInterface):

        try:
            self.payment_storage.check_if_upi_payment_method_already_exists(payment_type=payment_type, upi_id=upi_id)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            payment_presenter.raise_exception_for_upi_payment_method_already_exists()


    def create_cash_on_delivery_payment_method_wrapper(self, payment_type: str, payment_presenter: PaymentPresenterInterface):

        try:
            paymentmethod_id = self.create_cash_on_delivery_payment_method(payment_type=payment_type)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            payment_presenter.raise_exception_for_cash_on_delivery_payment_method_already_exists()
        else:
            return payment_presenter.get_response_for_create_cash_on_delivery_payment_method(paymentmethod_id=paymentmethod_id)

    def create_cash_on_delivery_payment_method(self, payment_type:str):

        """ELP
            check if paymentmethod exists
            create paymentmethod
        """
        self.payment_storage.check_if_cash_on_delivery_payment_method_already_exists(payment_type=payment_type)

        return self.payment_storage.create_cash_on_delivery_payment_method(payment_type=payment_type))

    def add_payment_method_to_order_wrapper(self, orderpayment_dto: OrderPaymentDTO, payment_presenter: PaymentPresenterInterface, 
                                            order_presenter: OrderPresenterInterface):

        try:
            payment_id = self.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)
        except custom_exceptions.OrderDoesNotExistException:
            order_presenter.raise_exception_for_order_does_not_exist()
        except custom_exceptions.PaymentMethodDoesNotExistException:
            payment_presenter.raise_exception_for_payment_method_does_not_exist()
        else:
            return payment_presenter.get_response_for_add_payment_method_to_order(payment_id=payment_id)

    def add_payment_method_to_order(self, orderpayment_dto: OrderPaymentDTO):

        """ELP
            check if order exists
            check if paymentmethod exists
            add payment to order
        """
        self._check_if_input_data_is_correct_for_add_payment_to_order(orderpayment_dto=orderpayment_dto)

        return self.payment_storage.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)

    def _check_if_input_data_is_correct_for_add_payment_to_order(self, orderpayment_dto: OrderPaymentDTO):
        
        self.order_storage.check_if_order_exists(order_id=orderpayment_dto.order_id)

        self.payment_storage.check_if_payment_method_exists(payment_method_id=orderpayment_dto.payment_method_id)