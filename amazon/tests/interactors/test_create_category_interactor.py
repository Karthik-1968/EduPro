from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest
from amazon.interactors.category_interactor import CategoryInteractor
from amazon.exceptions.custom_exceptions import CategoryAlreadyExistsException
from unittest.mock import create_autospec
import pytest

class TestCreateCategoryInteractor:

    def setup_method(self):
        self.storage = create_autospec(CategoryStorageInterface)
        self.interactor = CategoryInteractor(storage=self.storage)

    def test_if_create_category_already_exists_raises_exception(self):

        category_name = "electronics"

        presenter = create_autospec(CategoryPresenterInterface)

        self.storage.check_if_category_already_exists.side_effect = CategoryAlreadyExistsException
        presenter.raise_exception_for_category_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_category(category_name=category_name, presenter=presenter)

        self.storage.check_if_category_already_exists.assert_called_once_with(category_name=category_name)
        presenter.raise_exception_for_category_already_exists.assert_called_once()

    def test_create_category(self):
        
        category_name = "electronics"

        category_id = 1
        expected_output = {"category_id":category_id}

        presenter = create_autospec(CategoryPresenterInterface)

        self.storage.create_category.return_value = category_id
        presenter.get_response_for_create_category.return_value = expected_output

        actual_output = self.interactor.create_category(category_name=category_name, presenter=presenter)

        assert actual_output == expected_output

        self.storage.check_if_category_already_exists.assert_called_once_with(category_name=category_name)
        self.storage.create_category.assert_called_once_with(category_name=category_name)
        presenter.get_response_for_create_category.assert_called_once_with(category_id=category_id)