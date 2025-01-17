from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExistException
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import OrderIdDTO
from amazon.interactors.order_interactor import OrderInteractor
from mock import create_autospec
import pytest 

class TestGetOrdersOfUser:

    def setup_method(self):

        self.order_storage = create_autospec(OrderStorageInterface)
        self.user_storage = create_autospec(UserStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = OrderInteractor(user_storage=self.user_storage, order_storage=self.order_storage, item_storage=self.item_storage)

    def test_if_user_does_not_exist_raises_exception(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"

        user_presenter = create_autospec(UserPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        self.user_storage.check_if_user_exists.side_effect = UserDoesNotExistException
        user_presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.get_orders_of_user(user_id=user_id, user_presenter=user_presenter, order_presenter=order_presenter)

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        user_presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_get_orders_of_user(self):

        user_id = "550e8400-e29b-41d4-a716-446655440000"

        user_presenter = create_autospec(UserPresenterInterface)
        order_presenter = create_autospec(OrderPresenterInterface)

        order_dtos = [
            OrderIdDTO(order_id=1),
            OrderIdDTO(order_id=2),
            OrderIdDTO(order_id=3)
        ]

        expected_output = [
            {
                "order_id": 1
            },
            {
                "order_id": 2
            },
            {
                "order_id": 3
            }
        ]

        self.order_storage.get_orders_of_user.return_value = order_dtos
        order_presenter.get_response_for_get_orders_of_user.return_value = expected_output

        actual_output = self.interactor.get_orders_of_user(user_id=user_id, user_presenter=user_presenter, order_presenter=order_presenter)

        assert actual_output == expected_output

        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.order_storage.get_orders_of_user.assert_called_once_with(user_id=user_id)
        order_presenter.get_response_for_get_orders_of_user.assert_called_once_with(orderid_dtos=order_dtos)