from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.storage_interfaces.dtos import CategoryDTO
from amazon.models import Category
from amazon.exceptions import category_custom_exceptions

class CategoryStorageImplementation(CategoryStorageInterface):

    def check_if_category_already_exists(self, category_name):
        
        if Category.objects.filter(name=category_name).exists():
            raise category_custom_exceptions.CategoryAlreadyExistsException()

    def create_category(self, category_name:str)->int:
        
        category = Category.objects.create(
            name=category_name
        )

        return category.id

    def get_list_of_categories(self)->list[CategoryDTO]:
        
        categories = Category.objects.all()
        category_dtos = []

        for category in categories:
            category_dto = self._convert_category_object_to_dto(category)
            category_dtos.append(category_dto)
        
        return category_dtos
    
    def _convert_category_object_to_dto(category)->CategoryDTO:
        
        category_dto = CategoryDTO(
            category_name=category.name
        )

        return category_dto
    
    def check_if_category_exists(self, category_id):
        
        category = Category.objects.filter(id=category_id).exists()
        category_not_exists = not category

        if category_not_exists:
            raise category_custom_exceptions.CategoryDoesNotExistException(category_id=category_id)