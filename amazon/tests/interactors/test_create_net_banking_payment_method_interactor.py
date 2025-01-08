from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import PaymentMethodAlreadyExistsException
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.storage_interfaces.storage_interface import PaymentMethodDTO
from amazon.interactors.payment_interactor import PaymentInteractor
from mock import create_autospec
import pytest

class TestCreateNetBankingPaymentMethodInteractor:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = PaymentInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_net_banking_payment_method_already_exists_raises_exception(self):
        
        payment_type = "NET BANKING"
        bank_name = "SBI"
        username = "john_doe"
        password = "password"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, bank_name=bank_name, username=username, password=password)

        self.storage.check_if_net_banking_payment_method_already_exists.side_effect = PaymentMethodAlreadyExistsException
        self.presenter.raise_exception_for_net_banking_payment_method_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_net_banking_payment_method(payment_type=payment_type, bank_name=bank_name, username=username,\
                                                               password=password)
            
        self.storage.check_if_net_banking_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.raise_exception_for_net_banking_payment_method_already_exists.assert_called_once()

    def test_create_net_banking_payment_method(self):

        payment_type = "NET BANKING"
        bank_name = "SBI"
        username = "john_doe"
        password = "password"

        paymentmethod_dto = PaymentMethodDTO(payment_type=payment_type, bank_name=bank_name, username=username, password=password)

        paymentmethod_id = 1
        expected_output = {"payment_method_id": paymentmethod_id}

        self.storage.create_net_banking_payment_method.return_value = paymentmethod_id
        self.presenter.get_response_for_create_net_banking_payment_method.return_value = expected_output

        actual_output = self.interactor.create_net_banking_payment_method(payment_type=payment_type, bank_name=bank_name, username=username,\
                                                                         password=password)
        
        assert actual_output == expected_output

        self.storage.check_if_net_banking_payment_method_already_exists.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.storage.create_net_banking_payment_method.assert_called_once_with(paymentmethod_dto=paymentmethod_dto)
        self.presenter.get_response_for_create_net_banking_payment_method.assert_called_once()