from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.interactors.item_interactor import ItemInteractor
from amazon.interactors.storage_interfaces.storage_interface import ItemDTO
from mock import create_autospec
import pytest

class TestGetListOfItemsInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_get_list_of_interactors(self):

        item_dtos = [
            ItemDTO(item_name="item1", category_id=1, price=1000.0),
            ItemDTO(item_name="item2", category_id=1, price=2000.0)
        ]

        expected_output = [
                {
                    "item_name": "item1",
                    "price": 1000.0
                },
                {
                    "item_name": "item2",
                    "price": 2000.0
                }
            ]

        self.storage.get_list_of_items.return_value = item_dtos
        self.presenter.get_response_for_list_of_items.return_value = expected_output

        actual_output = self.interactor.get_list_of_items()

        assert actual_output == expected_output

        self.storage.get_list_of_items.assert_called_once()
        self.presenter.get_response_for_list_of_items.assert_called_once_with(item_dtos=item_dtos)
