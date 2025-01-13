from abc import abstractmethod
from amazon.interactors.storage_interfaces.dtos import CategoryDTO

class CategoryStorageInterface:

    @abstractmethod
    def check_if_category_already_exists(self, category_name:str):
        pass

    @abstractmethod
    def create_category(self, category_name:str)->int:
        pass

    @abstractmethod
    def get_list_of_categories(self)->list[CategoryDTO]:
        pass

    @abstractmethod
    def check_if_category_exists(self, category_id:int):
        pass