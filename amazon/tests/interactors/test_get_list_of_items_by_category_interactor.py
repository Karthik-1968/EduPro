from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.exceptions.custom_exceptions import CategoryDoesNotExistException
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.dtos import ItemDTO
import pytest

class TestGetListOfItemsByCategory:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = ItemInteractor(user_storage=self.user_storage, category_storage=self.category_storage, item_storage=self.item_storage)

    def test_if_category_does_not_exist_raise_exception(self):

        category_id = 1

        category_presenter = create_autospec(CategoryPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)

        self.category_storage.check_if_category_exists.side_effect = CategoryDoesNotExistException
        category_presenter.raise_exception_for_category_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.get_list_of_items_by_category(category_id=category_id, category_presenter=category_presenter,\
                                                           item_presenter=item_presenter)

        self.category_storage.check_if_category_exists.assert_called_once_with(category_id=category_id)
        category_presenter.raise_exception_for_category_does_not_exist.assert_called_once()

    def test_get_list_of_items_by_category(self):

        category_id = 1

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
        
        category_presenter = create_autospec(CategoryPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)

        self.item_storage.get_list_of_items_by_category.return_value = item_dtos
        item_presenter.get_response_for_list_of_items_by_category.return_value = expected_output

        actual_output = self.interactor.get_list_of_items_by_category(category_id=category_id, category_presenter=category_presenter,\
                                                                     item_presenter=item_presenter)

        assert actual_output == expected_output

        self.category_storage.check_if_category_exists.assert_called_once_with(category_id=category_id)
        self.item_storage.get_list_of_items_by_category.assert_called_once_with(category_id=category_id)
        item_presenter.get_response_for_list_of_items_by_category.assert_called_once_with(item_dtos=item_dtos)