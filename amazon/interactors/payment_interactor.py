from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExistsException, OrderDoesNotExistException, \
    PaymentMethodDoesNotExistException
from amazon.interactors.storage_interfaces.storage_interface import PaymentMethodDTO, OrderPaymentDTO
from typing import Optional


class PaymentInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_card_payment_method(self, payment_type:str, card_name:str, card_number:str, card_holder_name:str, cvv:int, \
                                   expiry_date:str, card_type:str):

        """ELP
            validate input data
            check if payment method already exists
            create payment method
        """
        self._validate_input_data_for_create_card_payment(payment_type=payment_type, card_name=card_name, card_number=card_number, \
                card_holder_name=card_holder_name, cvv=cvv, expiry_date=expiry_date)
        
        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, card_name=card_name, card_number=card_number, \
                                        card_holder_name=card_holder_name, cvv=cvv, expiry_date=expiry_date, card_type=card_type)

        self._check_if_input_data_is_correct_for_create_card_payment(paymentmethod_dto=paymentmethod_dto)

        paymentmethod_id = self.storage.create_card_payment_method(paymentmethod_dto=paymentmethod_dto)

        return self.presenter.get_response_for_create_card_payment_method(paymentmethod_id=paymentmethod_id)

    def _validate_input_data_for_create_card_payment(self, payment_type:str, card_name, card_number:str, card_holder_name:str, cvv:int, \
                                                    expiry_date:str):

        payment_type_not_present = not payment_type
        if payment_type_not_present:
            self.presenter.raise_exception_for_missing_payment_type()

        card_name_not_present = not card_name
        if card_name_not_present:
            self.presenter.raise_exception_for_missing_card_name()

        card_number_not_present = not card_number
        if card_number_not_present:
            self.presenter.raise_exception_for_missing_card_number()

        card_holder_name_not_present = not card_holder_name
        if card_holder_name_not_present:
            self.presenter.raise_exception_for_missing_card_holder_name()

        cvv_not_present = not cvv
        if cvv_not_present:
            self.presenter.raise_exception_for_missing_cvv()

        expiry_date_not_present = not expiry_date
        if expiry_date_not_present:
            self.presenter.raise_exception_for_missing_expiry_date()

    def _check_if_input_data_is_correct_for_create_card_payment(self, paymentmethod_dto:PaymentMethodDTO):
    
        try:
            self.storage.check_if_card_payment_method_already_exists(paymentmethod_dto=paymentmethod_dto)
        except PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_card_payment_method_already_exists()


    def create_net_banking_payment_method(self, payment_type:str, bank_name:str, username:str, password:str):

        """ELP
            validate input data
            check if payment method already exists
            create payment method
        """
        self._validate_input_data_for_create_net_banking_payment(payment_type=payment_type, bank_name=bank_name, username=username,\
                                                                 password=password)
        
        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, bank_name=bank_name, username=username, password=password)

        self._check_if_input_data_is_correct_for_create_net_banking_payment(paymentmethod_dto=paymentmethod_dto)

        paymentmethod_id = self.storage.create_net_banking_payment_method(paymentmethod_dto=paymentmethod_dto)

        return self.presenter.get_response_for_create_net_banking_payment_method(paymentmethod_id=paymentmethod_id)

    def _validate_input_data_for_create_net_banking_payment(self, payment_type:str, bank_name:str, username:str, password:str):

        payment_type_not_present = not payment_type
        if payment_type_not_present:
            self.presenter.raise_exception_for_missing_payment_type()

        bank_name_not_present = not bank_name
        if bank_name_not_present:
            self.presenter.raise_exception_for_missing_bank_name()

        username_not_present = not username
        if username_not_present:
            self.presenter.raise_exception_for_missing_username()

        password_not_present = not password
        if password_not_present:
            self.presenter.raise_exception_for_missing_password()

    def _check_if_input_data_is_correct_for_create_net_banking_payment(self, paymentmethod_dto:PaymentMethodDTO):

        try:
            self.storage.check_if_net_banking_payment_method_already_exists(paymentmethod_dto=paymentmethod_dto)
        except PaymentMethodAlreadyExistsException:
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
        except PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_upi_payment_method_already_exists()


    def create_cash_on_delivery_payment_method_wrapper(self, payment_type: str):

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type)

        try:
            paymentmethod_id = self.create_cash_on_delivery_payment_method(paymentmethod_dto=paymentmethod_dto)
        except PaymentMethodAlreadyExistsException:
            self.presenter.raise_exception_for_cash_on_delivery_payment_method_already_exists()
        else:
            return self.presenter.get_response_for_create_cash_on_delivery_payment_method(paymentmethod_id=paymentmethod_id)

    def create_cash_on_delivery_payment_method(self, paymentmethod_dto: PaymentMethodDTO):

        """ELP
            validate input data
            check if paymentmethod exists
            create paymentmethod
        """
        payment_type_not_exists = not paymentmethod_dto.payment_type
        if payment_type_not_exists:
            self.presenter.raise_exception_for_missing_payment_type()

        self.storage.check_if_cash_on_delivery_payment_method_already_exists(paymentmethod_dto=paymentmethod_dto)

        return self.storage.create_cash_on_delivery_payment_method(paymentmethod_dto=paymentmethod_dto)

        
    def add_payment_method_to_order(self, order_id:int, paymentmethod_id:int, status:str, amount:float, transaction_id:str,\
                                     gift_card_or_promo_code:Optional[str]):

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
        self._validate_input_details(order_id=order_id, paymentmethod_id=paymentmethod_id, status=status, amount=amount, \
            transaction_id=transaction_id)

        self._check_if_input_data_is_correct_for_add_payment_to_order(order_id=order_id, paymentmethod_id=paymentmethod_id)

        orderpayment_dto = OrderPaymentDTO(order_id=order_id, paymentmethod_id=paymentmethod_id, status=status, amount=amount, \
                                            transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)

        payment_id = self.storage.add_payment_method_to_order(orderpayment_dto=orderpayment_dto)

        return self.presenter.get_response_for_add_payment_method_to_order(payment_id=payment_id)

    def _validate_input_details(self, order_id:int, paymentmethod_id:int, status:str, amount:float, transaction_id:str):

        order_id_not_present = not order_id
        if order_id_not_present:
            self.presenter.raise_exception_for_missing_order_id()

        paymentmethod_id_not_present = not paymentmethod_id
        if paymentmethod_id_not_present:
            self.presenter.raise_exception_for_missing_paymentmethod_id()

        status_not_present = not status
        if status_not_present:
            self.presenter.raise_exception_for_missing_payment_status()

        amount_not_present = not amount
        if amount_not_present:
            self.presenter.raise_exception_for_missing_amount()

        transaction_id_not_present = not transaction_id
        if transaction_id_not_present:
            self.presenter.raise_exception_for_missing_transaction_id()

    def _check_if_input_data_is_correct_for_add_payment_to_order(self, order_id:int, paymentmethod_id:int):
        
        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_payment_method_exists(paymentmethod_id=paymentmethod_id)
        except PaymentMethodDoesNotExistException:
            self.presenter.raise_exception_for_payment_method_does_not_exist()