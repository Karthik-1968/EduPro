from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import CategoryAlreadyExists

class CategoryInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_category(self, category_name:str):

        """ELP
            validate_input_details
                -validate category_name
            check if category already exists
            create_category
        """
        category_not_present = not category_name
        if category_not_present:
            self.presenter.raise_exception_for_missing_category_name()

        try:
            self.storage.check_if_category_already_exists(category_name=category_name)
        except CategoryAlreadyExists:
            self.presenter.raise_exception_for_category_already_exists()

        category_id = self.storage.create_category(category_name=category_name)

        return self.presenter.get_response_for_create_category(category_id=category_id)

    def get_list_of_categories(self):

        category_dtos = self.storage.get_list_of_categories()

        return self.presenter.get_response_for_list_of_categories(category_dtos=category_dtos)