from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import CategoryDoesNotExistException
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import ItemDTO
import pytest

class TestGetListOfItemsByCategory:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = ItemInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_category_does_not_exist_raise_exception(self):

        category_id = 1

        self.storage.check_if_category_exists.side_effect = CategoryDoesNotExist
        self.presenter.raise_exception_for_category_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.get_list_of_items_by_category(category_id=category_id)

        self.storage.check_if_category_exists.assert_called_once_with(category_id=category_id)
        self.presenter.raise_exception_for_category_does_not_exist.assert_called_once()

    def test_get_list_of_items_by_category(self):

        category_id = 1

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

        self.storage.get_list_of_items_by_category.return_value = item_dtos
        self.presenter.get_response_for_list_of_items_by_category.return_value = expected_output

        actual_output = self.interactor.get_list_of_items_by_category(category_id=category_id)

        assert actual_output == expected_output

        self.storage.check_if_category_exists.assert_called_once_with(category_id=category_id)
        self.storage.get_list_of_items_by_category.assert_called_once_with(category_id=category_id)
        self.presenter.get_response_for_list_of_items_by_category.assert_called_once_with(item_dtos=item_dtos)