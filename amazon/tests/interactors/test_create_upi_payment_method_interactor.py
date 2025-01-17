from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.exceptions.payment_custom_exceptions import PaymentMethodAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest

class TestCreateUpiPaymentMethodInteractor:

    def setup_method(self):

        self.order_storage = create_autospec(OrderStorageInterface)
        self.payment_storage = create_autospec(PaymentStorageInterface)
        self.interactor = PaymentInteractor(order_storage=self.order_storage, payment_storage=self.payment_storage)

    def test_if_upi_payment_method_already_exists_raises_exception(self):

        payment_type = "UPI"
        upi_id = "john_doe@upi"

        payment_presenter = create_autospec(PaymentPresenterInterface)

        self.payment_storage.check_if_upi_payment_method_already_exists.side_effect = PaymentMethodAlreadyExistsException
        payment_presenter.raise_exception_for_upi_payment_method_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_upi_payment_method(payment_type=payment_type, upi_id=upi_id, payment_presenter=payment_presenter)
            
        self.payment_storage.check_if_upi_payment_method_already_exists.assert_called_once_with(payment_type=payment_type, upi_id=upi_id)
        payment_presenter.raise_exception_for_upi_payment_method_already_exists.assert_called_once()

    def test_create_upi_payment_method(self):

        payment_type = "UPI"
        upi_id = "john_doe@upi"

        payment_presenter = create_autospec(PaymentPresenterInterface)

        paymentmethod_id = 1
        expected_output = {"payment_method_id": paymentmethod_id}

        self.payment_storage.create_upi_payment_method.return_value = paymentmethod_id
        payment_presenter.get_response_for_create_upi_payment_method.return_value = expected_output

        actual_output = self.interactor.create_upi_payment_method(payment_type=payment_type, upi_id=upi_id, payment_presenter=payment_presenter)
        
        assert actual_output == expected_output

        self.payment_storage.check_if_upi_payment_method_already_exists.assert_called_once_with(payment_type=payment_type, upi_id=upi_id)
        self.payment_storage.create_upi_payment_method.assert_called_once_with(payment_type=payment_type, upi_id=upi_id)
        payment_presenter.get_response_for_create_upi_payment_method.assert_called_once_with(paymentmethod_id=paymentmethod_id)