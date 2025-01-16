from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.storage_interfaces.dtos import CardPaymentMethodDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest 

class TestCreateCardPaymentMethodInteractor:

    def setup_method(self):
        self.payment_storage = create_autospec(PaymentStorageInterface)
        self.order_storage = create_autospec(OrderStorageInterface)
        self.interactor = PaymentInteractor(payment_storage=self.payment_storage, order_storage=self.order_storage)

    def test_if_card_payment_method_already_exists_raises_exception(self):

        cardpayment_dto = CardPaymentMethodDTO(
                                payment_type = "CARD PAYMENT",
                                card_name = "SBI DEBIT CARD",
                                card_number = "1234567890123456",
                                card_holder_name = "John Doe",
                                expiry_date = "12/25",
                                cvv = "123",
                                card_type = "VISA")
        
        payment_presenter = create_autospec(PaymentPresenterInterface)
        
        self.payment_storage.check_if_card_payment_method_already_exists.side_effect = PaymentMethodAlreadyExistsException
        payment_presenter.raise_exception_for_card_payment_method_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_card_payment_method(cardpaymentmethod_dto=cardpayment_dto, payment_presenter=payment_presenter)
            
        self.payment_storage.check_if_card_payment_method_already_exists.assert_called_once_with(cardpaymentmethod_dto=cardpayment_dto)
        payment_presenter.raise_exception_for_card_payment_method_already_exists.assert_called_once()

    def test_create_card_payment_method(self):

        cardpayment_dto = CardPaymentMethodDTO(
                                payment_type = "CARD PAYMENT",
                                card_name = "SBI DEBIT CARD",
                                card_number = "1234567890123456",
                                card_holder_name = "John Doe",
                                expiry_date = "12/25",
                                cvv = "123",
                                card_type = "VISA")
        payment_presenter = create_autospec(PaymentPresenterInterface)

        paymentmethod_id = 1
        expected_output = {"payment_method_id": paymentmethod_id}

        self.payment_storage.create_card_payment_method.return_value = paymentmethod_id
        payment_presenter.get_response_for_create_card_payment_method.return_value = expected_output

        actual_output = self.interactor.create_card_payment_method(cardpaymentmethod_dto=cardpayment_dto, payment_presenter=payment_presenter)
        
        assert actual_output == expected_output

        self.payment_storage.check_if_card_payment_method_already_exists.assert_called_once_with(cardpaymentmethod_dto=cardpayment_dto)
        self.payment_storage.create_card_payment_method.assert_called_once_with(cardpaymentmethod_dto=cardpayment_dto)
        payment_presenter.get_response_for_create_card_payment_method.assert_called_once_with(paymentmethod_id=paymentmethod_id)