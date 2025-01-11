from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.interactors.category_interactor import CategoryInteractor
from amazon.interactors.storage_interfaces.dtos import CategoryDTO
from mock import create_autospec

class TestGetListOfCategoriesInteractor:

    def setup_method(self):

        self.storage = create_autospec(StorageInterface)
        self.presenter = create_autospec(PresenterInterface)
        self.interactor = CategoryInteractor(storage = self.storage, presenter = self.presenter)

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

        self.storage.get_list_of_categories.return_value = category_dtos
        self.presenter.get_response_for_list_of_categories.return_value = expected_output

        actual_output = self.interactor.get_list_of_categories()

        assert actual_output == expected_output

        self.storage.get_list_of_categories.assert_called_once()
        self.presenter.get_response_for_list_of_categories.assert_called_once_with(category_dtos=category_dtos)