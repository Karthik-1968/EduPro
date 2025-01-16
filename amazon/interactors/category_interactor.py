from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from amazon.exceptions.custom_exceptions import CategoryAlreadyExistsException

class CategoryInteractor:

    def __init__(self, storage: CategoryStorageInterface):

        self.storage = storage

    def create_category(self, category_name:str, presenter: CategoryPresenterInterface):

        """ELP
            check if category already exists
            create_category
        """
        try:
            self.storage.check_if_category_already_exists(category_name=category_name)
        except CategoryAlreadyExistsException:
            presenter.raise_exception_for_category_already_exists()

        category_id = self.storage.create_category(category_name=category_name)

        return presenter.get_response_for_create_category(category_id=category_id)


    def get_list_of_categories(self, presenter: CategoryPresenterInterface):

        category_dtos = self.storage.get_list_of_categories()

        return presenter.get_response_for_list_of_categories(category_dtos=category_dtos)