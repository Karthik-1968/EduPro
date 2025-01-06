from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemAlreadyExists
from amazon.interactors.item_interactor import ItemInteractor
from mock import create_autospec
from django.core.exceptions import BadRequest
import pytest 

class TestCreateItemInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_item_already_exists_raise_exception(self):

        item_name = "item1"
        category_id = 1
        price = 1000.0

        self.storage.check_if_item_already_exists.side_effect = ItemAlreadyExists
        self.presenter.raise_exception_for_item_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_item(item_name=item_name, category_id=category_id, price=price)

        self.storage.check_if_item_already_exists.assert_called_once_with(item_name=item_name)
        self.presenter.raise_exception_for_item_already_exists.assert_called_once()

    def test_create_item(self):

        item_name = "item1"
        category_id = 1
        price = 1000.0

        item_id = 1
        expected_output = {
            "item_id": item_id
        }

        self.storage.create_item.return_value = item_id
        self.presenter.get_response_for_create_item.return_value = expected_output

        actual_output = self.interactor.create_item(item_name=item_name, category_id=category_id, price=price)

        assert actual_output == expected_output

        self.storage.check_if_item_already_exists.assert_called_once_with(item_name=item_name)
        self.storage.create_item.assert_called_once_with(item_name=item_name, category_id=category_id, price=price)
        self.presenter.get_response_for_create_item.assert_called_once_with(item_id=item_id)