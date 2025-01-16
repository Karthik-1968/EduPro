from amazon.interactors.item_interactors.item_interactor import ItemInteractor
from mock import create_autospec
import pytest
from amazon.exceptions import custom_exceptions
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.storage_interfaces.dtos import ItemDTO

class TestGetItemDetailsInteractor:

    def setup_method(self):

        self.item_storage = create_autospec(ItemStorageInterface)
        self.user_storage = create_autospec(UserStorageInterface)
        self.category_storage = create_autospec(CategoryStorageInterface)
        self.interactor = ItemInteractor(item_storage=self.item_storage, user_storage=self.user_storage, \
                                            category_storage=self.category_storage)
        
    def test_if_item_does_not_exist_raises_exception(self):
        
        item_id = 1
        user_id = "f3f2e850-b5d4-11ef-ac7e-96584d5248b2"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        
        self.item_storage.check_if_item_exists.side_effect = custom_exceptions.ItemDoesNotExistException
        item_presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_item_details(item_id=item_id, user_id=user_id, user_presenter=user_presenter, \
                                             item_presenter=item_presenter)
            
        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        item_presenter.raise_exception_for_item_does_not_exist.assert_called_once()

    def test_if_user_does_not_exist_raises_exception(self):

        item_id = 1
        user_id = "f3f2e850-b5d4-11ef-ac7e-96584d5248b2"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
    
        self.user_storage.check_if_user_exists.side_effect = custom_exceptions.UserDoesNotExistException
        user_presenter.raise_exception_for_user_does_not_exist.side_effect = NotFound
        
        with pytest.raises(NotFound):
            self.interactor.get_item_details(item_id=item_id, user_id=user_id, user_presenter=user_presenter, \
                                             item_presenter=item_presenter)
            
        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        user_presenter.raise_exception_for_user_does_not_exist.assert_called_once()

    def test_get_item_details(self):

        item_id = 1
        user_id = "f3f2e850-b5d4-11ef-ac7e-96584d5248b2"

        user_presenter = create_autospec(UserPresenterInterface)
        item_presenter = create_autospec(ItemPresenterInterface)
        self.interactor.add_view_to_item = create_autospec(self.interactor.add_view_to_item)

        item_dto = ItemDTO(
            category_id=1,
            item_name="item",
            price=100.0,
            number_of_left_in_stock=10,
            views=5
        )

        expected_output = {
            "category_id": 1,
            "item_name": "item",
            "price": 100.0,
            "number_of_left_in_stock": 10,
            "views": 5
        }
        
        self.interactor.add_view_to_item.return_value = None
        self.item_storage.get_item_details.return_value = item_dto
        item_presenter.get_response_for_get_item_details.return_value = expected_output

        actual_output = self.interactor.get_item_details(item_id=item_id, user_id=user_id, user_presenter=user_presenter, \
                                                         item_presenter=item_presenter)

        assert actual_output == expected_output
        
        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=item_id)
        self.user_storage.check_if_user_exists.assert_called_once_with(user_id=user_id)
        self.interactor.add_view_to_item.assert_called_once_with(user_id=user_id, item_id=item_id)
        self.item_storage.get_item_details.assert_called_once_with(item_id=item_id)
        item_presenter.get_response_for_get_item_details.assert_called_once_with(item_dto=item_dto)