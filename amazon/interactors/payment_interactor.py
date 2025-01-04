from amazon.interactors.storage_interfaces import storage_interface
from amazon.interactors.presenters import presenter_interface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExists, OrderDoesNotExist, PaymentMethodDoesNotExist

class PaymentInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_payment(self, payment_type:str, card_number:str=None, card_holder_name:str=None, cvv:int=None, \
    expiry_date:str=None, bank_name:str=None, username:str=None, password:str=None, upi_id:str=None):

        """ELP
            check if payment method already exists
            create payment method
        """

        try:
            self.storage.check_if_payment_method_already_exists(payment_type=payment_type, card_number=card_number, \
            card_holder_name=card_holder_name, cvv=cvv, expiry_date=expiry_date, bank_name=bank_name, username=username,\
             password=password, upi_id=upi_id)
        except PaymentMethodAlreadyExists:
            self.presenter.raise_exception_for_payment_method_already_exists()

        paymentmethod_id = self.storage.create_payment_method(payment_type=payment_type, card_number=card_number, \
            card_holder_name=card_holder_name, cvv=cvv, expiry_date=expiry_date, bank_name=bank_name, username=username,\
             password=password, upi_id=upi_id)

        return self.presenter.get_response_for_create_payment_method(paymentmethod_id=paymentmethod_id)

    def add_payment_to_order(self, order_id:int, paymentmethod_id:int, status:str, amount:int, transaction_id:str):

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
        self.validate_input_details(order_id=order_id, paymentmethod_id=paymentmethod_id, status=status, amount=amount, \
            transaction_id=transaction_id)

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExist:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_paymentmethod_exists(paymentmethod_id=paymentmethod_id)
        except PaymentMethodDoesNotExist:
            self.presenter.raise_exception_for_paymentmethod_does_not_exist()

        payment_id = self.storage.add_payment_method_to_order(order_id=order_id, paymentmethod_id=paymentmethod_id, status=status, amount=amount, \
            transaction_id=transaction_id)

        return self.presenter.get_response_for_add_payment_to_order(payment_id=payment_id)

    def validate_input_details(self, order_id:int, paymentmethod_id:int, status:str, amount:int, transaction_id:str):

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