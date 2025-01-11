from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import CardPaymentMethodDTO, NetBankingPaymentMethodDTO, OrderPaymentDTO
from typing import Optional


class PaymentInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_card_payment_method(self, cardpaymentmethod_dto: CardPaymentMethodDTO):

        """ELP
            validate input data
            check if payment method already exists
            create payment method
        """
        self._validate_input_data_for_create_card_payment(cardpaymentmethod_dto=cardpaymentmethod_dto)

        self._check_if_input_data_is_correct_for_create_card_payment(cardpaymentmethod_dto=cardpaymentmethod_dto)

        paymentmethod_id = self.storage.create_card_payment_method(cardpaymentmethod_dto=cardpaymentmethod_dto)

        return self.presenter.get_response_for_create_card_payment_method(paymentmethod_id=paymentmethod_id)

    def _validate_input_data_for_create_card_payment(self, cardpaymentmethod_dto: CardPaymentMethodDTO):

        payment_type_not_present = not cardpaymentmethod_dto.payment_type
        if payment_type_not_present:
            self.presenter.raise_exception_for_missing_payment_type()

        card_name_not_present = not cardpaymentmethod_dto.card_name
        if card_name_not_present:
            self.presenter.raise_exception_for_missing_card_name()

        card_number_not_present = not cardpaymentmethod_dto.card_number
        if card_number_not_present:
            self.presenter.raise_exception_for_missing_card_number()

        card_holder_name_not_present = not cardpaymentmethod_dto.card_holder_name
        if card_holder_name_not_present:
            self.presenter.raise_exception_for_missing_card_holder_name()

        cvv_not_present = not cardpaymentmethod_dto.cvv
        if cvv_not_present:
            self.presenter.raise_exception_for_missing_cvv()

        expiry_date_not_present = not cardpaymentmethod_dto.expiry_date
        if expiry_date_not_present:
            self.presenter.raise_exception_for_missing_expiry_date()

    def _check_if_input_data_is_correct_for_create_card_payment(self, cardpaymentmethod_dto:CardPaymentMethodDTO):
    
        try:
            self.storage.check_if_card_payment_method_already_exists(cardpaymentmethod_dto=cardpaymentmethod_dto)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_card_payment_method_already_exists()


    def create_net_banking_payment_method(self, netbankingpaymentmethod_dto: NetBankingPaymentMethodDTO):

        """ELP
            validate input data
            check if payment method already exists
            create payment method
        """
        self._validate_input_data_for_create_net_banking_payment(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)

        self._check_if_input_data_is_correct_for_create_net_banking_payment(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)

        paymentmethod_id = self.storage.create_net_banking_payment_method(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)

        return self.presenter.get_response_for_create_net_banking_payment_method(paymentmethod_id=paymentmethod_id)

    def _validate_input_data_for_create_net_banking_payment(self, netbankingpaymentmethod_dto: NetBankingPaymentMethodDTO):

        payment_type_not_present = not netbankingpaymentmethod_dto.payment_type
        if payment_type_not_present:
            self.presenter.raise_exception_for_missing_payment_type()

        bank_name_not_present = not netbankingpaymentmethod_dto.bank_name
        if bank_name_not_present:
            self.presenter.raise_exception_for_missing_bank_name()

        username_not_present = not netbankingpaymentmethod_dto.username
        if username_not_present:
            self.presenter.raise_exception_for_missing_username()

        password_not_present = not netbankingpaymentmethod_dto.password
        if password_not_present:
            self.presenter.raise_exception_for_missing_password()

    def _check_if_input_data_is_correct_for_create_net_banking_payment(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO):

        try:
            self.storage.check_if_net_banking_payment_method_already_exists(netbankingpaymentmethod_dto=netbankingpaymentmethod_dto)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_net_banking_payment_method_already_exists()


    def create_upi_payment_method(self, payment_type:str, upi_id:str):

        """ELP
            valiate input data
            check if payment method already exists
            create payment method
        """
        self._validate_input_data_for_create_upi_payment(payment_type=payment_type, upi_id=upi_id)
        
        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, upi_id=upi_id)

        self._check_if_input_data_is_correct_for_create_upi_payment(paymentmethod_dto=paymentmethod_dto)

        paymentmethod_id = self.storage.create_upi_payment_method(paymentmethod_dto=paymentmethod_dto)

        return self.presenter.get_response_for_create_upi_payment_method(paymentmethod_id=paymentmethod_id)

    def _validate_input_data_for_create_upi_payment(self, payment_type:str, upi_id:str):
        
        payment_type_not_present = not payment_type
        if payment_type_not_present:
            self.presenter.raise_exception_for_missing_payment_type()

        upi_id_not_present = not upi_id
        if upi_id_not_present:
            self.presenter.raise_exception_for_missing_upi_id()

    def _check_if_input_data_is_correct_for_create_upi_payment(self, paymentmethod_dto:PaymentMethodDTO):

        try:
            self.storage.check_if_upi_payment_method_already_exists(paymentmethod_dto=paymentmethod_dto)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_upi_payment_method_already_exists()


    def create_cash_on_delivery_payment_method_wrapper(self, payment_type: str):

        try:
            paymentmethod_id = self.create_cash_on_delivery_payment_method(payment_type=payment_type)
        except custom_exceptions.PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_cash_on_delivery_payment_method_already_exists()
        else:
            return self.presenter.get_response_for_create_cash_on_delivery_payment_method(paymentmethod_id=paymentmethod_id)

    def create_cash_on_delivery_payment_method(self, payment_type:str):

        """ELP
            validate input data
            check if paymentmethod exists
            create paymentmethod
        """
        payment_type_not_exists = not payment_type
        if payment_type_not_exists:
            self.presenter.raise_exception_for_missing_payment_type()

        self.storage.check_if_cash_on_delivery_payment_method_already_exists(payment_type=payment_type)

        return self.storage.create_cash_on_delivery_payment_method(payment_type=payment_type))

    def add_payment_method_to_order_wrapper(self, orderpayment_dto: OrderPaymentDTO):

        try:
            payment_id = self.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()
        except custom_exceptions.PaymentMethodDoesNotExistException:
            self.presenter.raise_exception_for_payment_method_does_not_exist()
        else:
            return self.presenter.get_response_for_add_payment_method_to_order(payment_id=payment_id)

    def add_payment_method_to_order(self, orderpayment_dto: OrderPaymentDTO):

        """ELP
            validate input details
                 -validate order_id
                 -validate paymentmethod_id
                 -validate status
                 -validate amount
                 -validate transaction_id
            check if order exists
            check if paymentmethod exists
            add payment to order
        """    
        self._validate_input_details_for_add_payment_to_order(orderpayment_dto=orderpayment_dto)

        self._check_if_input_data_is_correct_for_add_payment_to_order(orderpayment_dto=orderpayment_dto)

        return self.storage.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)

    def _validate_input_details_for_add_payment_to_order(self, orderpayment_dto: OrderPaymentDTO):

        order_id_not_present = not orderpayment_dto.order_id
        if order_id_not_present:
            self.presenter.raise_exception_for_missing_order_id()

        payment_method_id_not_present = not orderpayment_dto.payment_method_id
        if payment_method_id_not_present:
            self.presenter.raise_exception_for_missing_payment_method_id()

        payment_status_not_present = not orderpayment_dto.payment_status
        if payment_status_not_present:
            self.presenter.raise_exception_for_missing_payment_status()

        amount_not_present = not orderpayment_dto.amount
        if amount_not_present:
            self.presenter.raise_exception_for_missing_amount()

        transaction_id_not_present = not orderpayment_dto.transaction_id
        if transaction_id_not_present:
            self.presenter.raise_exception_for_missing_transaction_id()

    def _check_if_input_data_is_correct_for_add_payment_to_order(self, orderpayment_dto: OrderPaymentDTO):
        
        self.storage.check_if_order_exists(order_id=orderpayment_dto.order_id)

        self.storage.check_if_payment_method_exists(payment_method_id=orderpayment_dto.payment_method_id)