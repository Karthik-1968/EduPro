from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodDoesNotExistException, OrderDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import OrderPaymentDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest


class TestAddPaymentMethodToOrderInteractor:

    def setup_method(self):

        self.order_storage = create_autospec(OrderStorageInterface)
        self.payment_storage = create_autospec(PaymentStorageInterface)
        self.interactor = PaymentInteractor(order_storage=self.order_storage, payment_storage=self.payment_storage)

    def test_if_order_does_not_exist_raises_exception(self):

        orderpayment_dto = OrderPaymentDTO(
                                order_id = 1,
                                paymentmethod_id = 1,
                                amount = 1000.0,
                                payment_status = "PENDING",
                                transaction_id = "12345",
                                gift_card_or_promo_code = None)

        order_presenter = create_autospec(OrderPresenterInterface)
        payment_presenter = create_autospec(PaymentPresenterInterface)

        self.order_storage.check_if_order_exists.side_effect = OrderDoesNotExistException
        order_presenter.raise_exception_for_order_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_payment_method_to_order_wrapper(orderpayment_dto=orderpayment_dto, order_presenter=order_presenter, \
                                                                payment_presenter=payment_presenter)
            
        self.order_storage.check_if_order_exists.assert_called_once_with(order_id=orderpayment_dto.order_id)
        order_presenter.raise_exception_for_order_does_not_exist.assert_called_once()

    def test_if_payment_method_does_not_exist_raises_exception(self):

        orderpayment_dto = OrderPaymentDTO(
                                order_id = 1,
                                paymentmethod_id = 1,
                                amount = 1000.0,
                                payment_status = "PENDING",
                                transaction_id = "12345",
                                gift_card_or_promo_code = None)

        order_presenter = create_autospec(OrderPresenterInterface)
        payment_presenter = create_autospec(PaymentPresenterInterface)

        self.payment_storage.check_if_payment_method_exists.side_effect = PaymentMethodDoesNotExistException
        payment_presenter.raise_exception_for_payment_method_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_payment_method_to_order_wrapper(orderpayment_dto=orderpayment_dto, order_presenter=order_presenter, \
                                                        payment_presenter=payment_presenter)
            
        self.payment_storage.check_if_payment_method_exists.assert_called_once_with(paymentmethod_id=orderpayment_dto.paymentmethod_id)
        payment_presenter.raise_exception_for_payment_method_does_not_exist.assert_called_once()

    def test_add_payment_to_order(self):

        orderpayment_dto = OrderPaymentDTO(
                                order_id = 1,
                                paymentmethod_id = 1,
                                amount = 1000.0,
                                payment_status = "PENDING",
                                transaction_id = "12345",
                                gift_card_or_promo_code = None)

        order_presenter = create_autospec(OrderPresenterInterface)
        payment_presenter = create_autospec(PaymentPresenterInterface)

        payment_id = 1
        expected_output={
            "payment_id": payment_id
        }

        self.payment_storage.add_payment_method_to_order.return_value = payment_id
        payment_presenter.get_response_for_add_payment_method_to_order.return_value = expected_output

        actual_output = self.interactor.add_payment_method_to_order_wrapper(orderpayment_dto=orderpayment_dto, \
                                                                    order_presenter=order_presenter, payment_presenter=payment_presenter)
        
        assert actual_output == expected_output

        self.order_storage.check_if_order_exists.assert_called_once_with(order_id=orderpayment_dto.order_id)
        self.payment_storage.check_if_payment_method_exists.assert_called_once_with(paymentmethod_id=orderpayment_dto.paymentmethod_id)
        self.payment_storage.add_payment_method_to_order.assert_called_once_with(orderpayment_dto=orderpayment_dto)
        payment_presenter.get_response_for_add_payment_method_to_order.assert_called_once_with(payment_id=payment_id)
