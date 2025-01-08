from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodDoesNotExistException, OrderDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.storage_interface import OrderPaymentDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest


class TestAddPaymentMethodToOrderInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = PaymentInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_order_does_not_exist_raises_exception(self):

        order_id = 1
        paymentmethod_id = 1
        amount = 1000.0
        status = "PENDING"
        transaction_id = "12345"
        gift_card_or_promo_code = None

        self.storage.check_if_order_exists.side_effect = OrderDoesNotExistException
        self.presenter.raise_exception_for_order_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_payment_method_to_order(order_id=order_id, paymentmethod_id=paymentmethod_id, amount=amount, status=status,\
             transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)
            
        self.storage.check_if_order_exists.assert_called_once_with(order_id=order_id)
        self.presenter.raise_exception_for_order_does_not_exist.assert_called_once()

    def test_if_payment_method_does_not_exist_raises_exception(self):

        order_id = 1
        paymentmethod_id = 1
        amount = 1000.0
        status = "PENDING"
        transaction_id = "12345"
        gift_card_or_promo_code = None

        self.storage.check_if_payment_method_exists.side_effect = PaymentMethodDoesNotExistException
        self.presenter.raise_exception_for_payment_method_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_payment_method_to_order(order_id=order_id, paymentmethod_id=paymentmethod_id, amount=amount, \
                        status=status, transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)
            
        self.storage.check_if_payment_method_exists.assert_called_once_with(paymentmethod_id=paymentmethod_id)
        self.presenter.raise_exception_for_payment_method_does_not_exist.assert_called_once()

    def test_add_payment_to_order(self):

        order_id = 1
        paymentmethod_id = 1
        amount = 1000.0
        status = "PENDING"
        transaction_id = "12345"
        gift_card_or_promo_code = None

        orderpayment_dto = OrderPaymentDTO(order_id=order_id, paymentmethod_id=paymentmethod_id, amount=amount, status=status,\
         transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)

        payment_id = 1
        expected_output = {"payment_id": payment_id}

        self.storage.add_payment_method_to_order.return_value = payment_id
        self.presenter.get_response_for_add_payment_method_to_order.return_value = expected_output

        actual_output = self.interactor.add_payment_method_to_order(order_id=order_id, paymentmethod_id=paymentmethod_id, amount=amount, status=status,\
        transaction_id=transaction_id, gift_card_or_promo_code=gift_card_or_promo_code)
        
        assert actual_output == expected_output

        self.storage.check_if_order_exists.assert_called_once_with(order_id=order_id)
        self.storage.check_if_payment_method_exists.assert_called_once_with(paymentmethod_id=paymentmethod_id)
        self.storage.add_payment_method_to_order.assert_called_once_with(orderpayment_dto=orderpayment_dto)
        self.presenter.get_response_for_add_payment_method_to_order.assert_called_once_with(payment_id=payment_id)
