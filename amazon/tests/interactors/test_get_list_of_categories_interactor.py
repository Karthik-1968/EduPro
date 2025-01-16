from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from amazon.interactors.category_interactor import CategoryInteractor
from amazon.interactors.storage_interfaces.dtos import CategoryDTO
from mock import create_autospec

class TestGetListOfCategoriesInteractor:

    def setup_method(self):

        self.storage = create_autospec(CategoryStorageInterface)
        self.interactor = CategoryInteractor(storage = self.storage)

    def test_get_list_of_categories(self):

        category_dtos = [
            CategoryDTO(category_name="electronics"),
            CategoryDTO(category_name="fashion"),
            CategoryDTO(category_name="home")
        ]

        expected_output = [
            {"category_name": "electronics"},
            {"category_name": "fashion"},
            {"category_name": "home"}
        ]

        presenter = create_autospec(CategoryPresenterInterface)

        self.storage.get_list_of_categories.return_value = category_dtos
        presenter.get_response_for_list_of_categories.return_value = expected_output

        actual_output = self.interactor.get_list_of_categories(presenter=presenter)

        assert actual_output == expected_output

        self.storage.get_list_of_categories.assert_called_once()
        presenter.get_response_for_list_of_categories.assert_called_once_with(category_dtos=category_dtos)