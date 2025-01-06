from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django.core.exceptions import BadRequest
from amazon.interactors.category_interactor import CategoryInteractor
from amazon.exceptions.custom_exceptions import CategoryAlreadyExists
from unittest.mock import create_autospec
import pytest

class TestCreateCategoryInteractor:

    def setup_method(self):
        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = CategoryInteractor(storage=self.storage, presenter=self.presenter)

    def test_if_create_category_already_exists_raises_exception(self):

        category_name = "electronics"

        self.storage.check_if_category_already_exists.side_effect = CategoryAlreadyExists
        self.presenter.raise_exception_for_category_already_exists.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.create_category(category_name=category_name)

        self.storage.check_if_category_already_exists.assert_called_once_with(category_name=category_name)
        self.presenter.raise_exception_for_category_already_exists.assert_called_once()

    def test_create_category(self):
        
        category_name = "electronics"

        category_id = 1

        expected_output = {"category_id":category_id}

        self.storage.create_category.return_value = category_id
        self.presenter.get_response_for_create_category.return_value = expected_output

        actual_output = self.interactor.create_category(category_name=category_name)

        assert actual_output == expected_output

        self.storage.check_if_category_already_exists.assert_called_once_with(category_name=category_name)
        self.storage.create_category.assert_called_once_with(category_name=category_name)
        self.presenter.get_response_for_create_category.assert_called_once_with(category_id=category_id)