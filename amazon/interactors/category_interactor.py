from amazon.interactors.storage_interfaces import storage_interface
from amazon.interactors.presenter_interfaces import presenter_interface
from amazon.exceptions.custom_exception import CategoryAlreadyExists

class CategoryInteractor:

    def __init__(self, storage: storage_interface, presenter: presenter_interface):
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