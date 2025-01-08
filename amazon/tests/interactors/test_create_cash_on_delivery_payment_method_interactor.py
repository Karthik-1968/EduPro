from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.storage_interfaces.storage_interface import PaymentMethodDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest

class TestCashOnDeliveryPaymentMethod:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = PaymentInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_cash_on_delivery_payment_method_already_exists_raises_exception(self):
        
        payment_type = "CASH ON DELIVERY"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type)

        self.storage.check_if_cash_on_delivery_payment_method_already_exists.side_effect = PaymentMethodAlreadyExistsException
        self.presenter.raise_exception_for_cash_on_delivery_payment_method_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_cash_on_delivery_payment_method_wrapper(payment_type=payment_type)
            
        self.storage.check_if_cash_on_delivery_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.raise_exception_for_cash_on_delivery_payment_method_already_exists.assert_called_once()

    def test_create_cash_on_delivery_payment_method(self):

        payment_type = "CASH ON DELIVERY"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type)

        paymentmethod_id = 1
        expected_output = {"payment_method_id": paymentmethod_id}

        self.storage.create_cash_on_delivery_payment_method.return_value = paymentmethod_id
        self.presenter.get_response_for_create_cash_on_delivery_payment_method.return_value = expected_output

        actual_output = self.interactor.create_cash_on_delivery_payment_method_wrapper(payment_type=payment_type)
        
        assert actual_output == expected_output

        self.storage.check_if_cash_on_delivery_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.storage.create_cash_on_delivery_payment_method.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.get_response_for_create_cash_on_delivery_payment_method.assert_called_once()