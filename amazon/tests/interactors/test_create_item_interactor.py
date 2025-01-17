from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.exceptions.item_custom_exceptions import ItemAlreadyExistsException
from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from amazon.interactors.storage_interfaces.dtos import ItemDTO
from mock import create_autospec
from django.core.exceptions import BadRequest
import pytest 

class TestCreateItemInteractor:

    def setup_method(self):

        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.item_storage = create_autospec(ItemStorageInterface)
        self.interactor = ItemInteractor(user_storage=self.user_storage, category_storage=self.category_storage, item_storage=self.item_storage)

    def test_if_item_already_exists_raise_exception(self):

        item_dto = ItemDTO(
            item_name = "item1",
            category_id = 1,
            price = 1000.0,
            number_of_left_in_stock = 10,
            number_of_purchases_in_last_month=5,
            views = 10)
        
        item_presenter = create_autospec(ItemPresenterInterface)
        category_presenter = create_autospec(CategoryPresenterInterface)

        self.item_storage.check_if_item_already_exists.side_effect = ItemAlreadyExistsException
        item_presenter.raise_exception_for_item_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_item(item_dto=item_dto, item_presenter=item_presenter, category_presenter=category_presenter)

        self.item_storage.check_if_item_already_exists.assert_called_once_with(item_name=item_dto.item_name)
        item_presenter.raise_exception_for_item_already_exists.assert_called_once()

    def test_create_item(self):

        item_dto = ItemDTO(
            item_name = "item1",
            category_id = 1,
            price = 1000.0,
            number_of_left_in_stock = 10,
            number_of_purchases_in_last_month=5,
            views = 10)

        item_id = 1
        expected_output = {
            "item_id": item_id
        }

        item_presenter = create_autospec(ItemPresenterInterface)
        category_presenter = create_autospec(CategoryPresenterInterface)

        self.item_storage.create_item.return_value = item_id
        item_presenter.get_response_for_create_item.return_value = expected_output

        actual_output = self.interactor.create_item(item_dto=item_dto, item_presenter=item_presenter, category_presenter=category_presenter)

        assert actual_output == expected_output

        self.item_storage.check_if_item_already_exists.assert_called_once_with(item_name=item_dto.item_name)
        self.item_storage.create_item.assert_called_once_with(item_dto=item_dto)
        item_presenter.get_response_for_create_item.assert_called_once_with(item_id=item_id)