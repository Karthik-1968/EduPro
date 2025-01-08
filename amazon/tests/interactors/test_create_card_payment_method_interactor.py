from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.storage_interfaces.storage_interface import PaymentMethodDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest 

class TestCreateCardPaymentMethodInteractor:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = PaymentInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_card_payment_method_already_exists_raises_exception(self):

        payment_type = "CARD PAYMENT"
        card_name = "SBI DEBIT CARD"
        card_number = "1234567890123456"
        card_holder_name = "John Doe"
        expiry_date = "12/25"
        cvv = "123"
        card_type = "VISA"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type,  card_name=card_name, card_number=card_number, card_holder_name=card_holder_name,\
         expiry_date=expiry_date, cvv=cvv, card_type=card_type)
        
        self.storage.check_if_card_payment_method_already_exists.side_effect = PaymentMethodAlreadyExistsException
        self.presenter.raise_exception_for_card_payment_method_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_card_payment_method(payment_type=payment_type, card_number=card_number, card_holder_name=card_holder_name,\
             expiry_date=expiry_date, cvv=cvv, card_type=card_type, card_name=card_name)
            
        self.storage.check_if_card_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.raise_exception_for_card_payment_method_already_exists.assert_called_once()

    def test_create_card_payment_method(self):

        payment_type = "CARD PAYMENT"
        card_name = "SBI DEBIT CARD"
        card_number = "1234567890123456"
        card_holder_name = "John Doe"
        expiry_date = "12/25"
        cvv = "123"
        card_type = "VISA"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, card_number=card_number, card_holder_name=card_holder_name,\
         expiry_date=expiry_date, cvv=cvv, card_type=card_type, card_name=card_name)

        paymentmethod_id = 1
        expected_output = {"payment_method_id": paymentmethod_id}

        self.storage.create_card_payment_method.return_value = paymentmethod_id
        self.presenter.get_response_for_create_card_payment_method.return_value = expected_output

        actual_output = self.interactor.create_card_payment_method(payment_type=payment_type, card_number=card_number, \
                        card_holder_name=card_holder_name, expiry_date=expiry_date, cvv=cvv, card_type=card_type, card_name=card_name)
        
        assert actual_output == expected_output

        self.storage.check_if_card_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.storage.create_card_payment_method.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.get_response_for_create_card_payment_method.assert_called_once_with(paymentmethod_id=paymentmethod_id)