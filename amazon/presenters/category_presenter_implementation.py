from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.storage_interfaces.dtos import CategoryDTO
from amazon.constants import exception_messages

class CategoryPresenterImplementation(CategoryPresenterInterface):
    
    def raise_exception_for_category_already_exists(self):
        raise BadRequest(*exception_messages.CATEGORY_ALREADY_EXISTS)
    
    def raise_exception_for_category_does_not_exist(self):
        raise NotFound(*exception_messages.CATEGORY_DOES_NOT_EXIST)
    
    def get_response_for_create_category(self, category_id:int):
        return {
            "category_id": category_id
        }
    
    def get_response_for_list_of_categories(self, category_dtos:CategoryDTO)->list[dict]:

        list_of_categories = []

        for category_dto in category_dtos:
            category_dto = {
                "category_name": category_dto.category_name
            }
            list_of_categories.append(category_dto)

        return list_of_categories