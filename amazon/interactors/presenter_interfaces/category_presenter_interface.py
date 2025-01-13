from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import CategoryDTO

class CategoryPresenterInterface:

    @abstractmethod
    def raise_exception_for_category_already_exists(self):
        pass

    @abstractmethod
    def get_response_for_create_category(self, category_id:int):
        pass

    @abstractmethod
    def get_response_for_list_of_categories(self, category_dtos:list[CategoryDTO])->list[dict]:
        pass

    @abstractmethod
    def raise_exception_for_category_does_not_exist(self):
        pass