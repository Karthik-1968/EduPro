from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import OrderDTO
from amazon.interactors.order_interactor import OrderInteractor
from mock import create_autospec
import pytest 

class TestGetOrdersOfUser:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = OrderInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_user_does_not_exist(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"

        self.storage.check_if_user_exists.side_effect = UserDoesNotExistException
        self.presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.get_orders_of_user(user_id=user_id)

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_get_orders_of_user(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"

        order_dtos = [
            OrderDTO(user_id=user_id, item_id=1, address_id=1, status="ORDERED", delivery_date="2020-12-12",\
             item_properties=[1, 2], delivery_charges=None, receiving_person_name=None, item_warranty_id=2),
            OrderDTO(user_id=user_id, item_id=2, address_id=1, status="ORDERED", delivery_date="2020-12-12",\
             item_properties=[1, 2], delivery_charges=None, receiving_person_name=None, item_warranty_id=1)
        ]

        expected_output = [
            {
                "item_id": 1,
                "address_id": 1,
                "status": "ORDERED",
                "delivery_date": "2020-12-12",
                "item_properties": [1, 2],
                "delivery_charges": None,
                "receiving_person_name": None,
                "item_warranty_id": 2
            },
            {
                "item_id": 2,
                "address_id": 1,
                "status": "ORDERED",
                "delivery_date": "2020-12-12",
                "item_properties": [1, 2],
                "delivery_charges": None,
                "receiving_person_name": None,
                "item_warranty_id": 1
            }
        ]

        self.storage.get_orders_of_user.return_value = order_dtos
        self.presenter.get_response_for_get_orders_of_user.return_value = expected_output

        actual_output = self.interactor.get_orders_of_user(user_id=user_id)

        assert actual_output == expected_output

        self.storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.storage.get_orders_of_user.assert_called_once_with(user_id=user_id)
        self.presenter.get_response_for_get_orders_of_user.assert_called_once_with(order_dtos=order_dtos)