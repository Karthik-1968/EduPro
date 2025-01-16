from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from amazon.interactors.storage_interfaces.dtos import ItemDTO
from mock import create_autospec
import pytest

class TestGetListOfItemsInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = ItemInteractor(user_storage=self.user_storage, category_storage=self.category_storage, item_storage=self.item_storage)

    def test_get_list_of_interactors(self):

        item_dtos = [
            ItemDTO(item_name="item1", category_id=1, price=1000.0, number_of_left_in_stock=10, views=0),
            ItemDTO(item_name="item2", category_id=1, price=2000.0, number_of_left_in_stock=10, views=0)
        ]

        expected_output = [
                {
                    "item_name": "item1",
                    "price": 1000.0,
                    "number_of_left_in_stock": 10,
                    "views": 0
                },
                {
                    "item_name": "item2",
                    "price": 2000.0,
                    "number_of_left_in_stock": 10,
                    "views": 0
                }
            ]
        
        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.get_list_of_items.return_value = item_dtos
        item_presenter.get_response_for_list_of_items.return_value = expected_output

        actual_output = self.interactor.get_list_of_items(item_presenter=item_presenter)

        assert actual_output == expected_output

        self.item_storage.get_list_of_items.assert_called_once()
        item_presenter.get_response_for_list_of_items.assert_called_once_with(item_dtos=item_dtos)
