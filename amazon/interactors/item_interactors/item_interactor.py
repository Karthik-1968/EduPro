from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.category_storage_interface import CategoryStorageInterface
from amazon.interactors.presenter_interfaces.category_presenter_interface import CategoryPresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import ItemDTO

class ItemInteractor:

    def __init__(self, user_storage:UserStorageInterface, user_presenter:UserPresenterInterface, item_storage: ItemStorageInterface,\
                 item_presenter: ItemPresenterInterface, category_storage: CategoryStorageInterface, \
                 category_presenter: CategoryPresenterInterface):
        
        self.user_storage = user_storage
        self.user_presenter = user_presenter
        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.category_storage = category_storage
        self.category_presenter = category_presenter


    def create_item(self, item_dto:ItemDTO):
        
        """ELP
            check if item already exists
            create_item
        """
        try:
            self.category_storage.check_if_category_exists(category_id=item_dto.category_id)
        except custom_exceptions.CategoryDoesNotExistException:
            self.category_presenter.raise_exception_for_category_does_not_exist()

        try:
            self.item_storage.check_if_item_already_exists(item_name=item_dto.item_name)
        except custom_exceptions.ItemAlreadyExistsException:
            self.item_presenter.raise_exception_for_item_already_exists()

        item_id = self.item_storage.create_item(item_dto=item_dto)

        return self.item_presenter.get_response_for_create_item(item_id=item_id)

    def get_item_details(self, item_id: str, user_id: str):

        """ELP
            -check if user exists
            -check if item exists
            -get item details
        """
        self._check_if_input_data_is_correct(item_id=item_id, user_id=user_id)

        self.add_view_to_item(user_id=user_id, item_id=item_id)

        item_dto = self.item_storage.get_item_details(item_id=item_id)

        return self.item_presenter.get_response_for_get_item_details(item_dto=item_dto)

    def _check_if_input_data_is_correct(self, item_id:int, user_id:str):

        try:
            self.user_storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()


    def get_list_of_items(self):

        item_dtos = self.item_storage.get_list_of_items()

        return self.item_presenter.get_response_for_list_of_items(item_dtos=item_dtos)


    def get_list_of_items_by_category(self, category_id:int):

        """ELP
            check if category exists
            get_list_of_items_by_category
        """
        try:
            self.category_storage.check_if_category_exists(category_id=category_id)
        except custom_exceptions.CategoryDoesNotExistException:
            self.category_presenter.raise_exception_for_category_does_not_exist()

        item_dtos = self.item_storage.get_list_of_items_by_category(category_id=category_id)

        return self.item_presenter.get_response_for_list_of_items_by_category(item_dtos=item_dtos)

    def create_property(self, property_name:str):
        
        """ELP
            check if property already exists
            create_property
        """
        try:
            self.item_storage.check_if_property_already_exists(property_name=property_name)
        except custom_exceptions.PropertyAlreadyExistsException:
            self.item_presenter.raise_exception_for_property_already_exists()

        property_id = self.item_storage.create_property(property_name=property_name)

        return self.item_presenter.get_response_for_create_property(property_id=property_id)

    def add_property_to_item(self, item_id:int, property_id:int, value:str):

        """ELP
            check if item exists
            check if property exists
            check if property already added to item
            add_property_to_item
        """
        self._check_if_input_data_is_correct_for_add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        itemproperty_id = self.item_storage.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        return self.item_presenter.get_response_for_add_property_to_item(itemproperty_id=itemproperty_id)

    def _check_if_input_data_is_correct_for_add_property_to_item(self, item_id:int, property_id:int, value:str):

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_property_exists(property_id=property_id)
        except custom_exceptions.PropertyDoesNotExistException:
            self.item_presenter.raise_exception_for_property_does_not_exist()

        try:
            self.item_storage.check_if_property_already_added_to_item(item_id=item_id, property_id=property_id, value=value)
        except custom_exceptions.PropertyAlreadyAddedToItemException:
            self.item_presenter.raise_exception_for_property_already_added_to_item()


    def delete_item_property(self, item_property_id:int):

        """ELP
            check if itemproperty exists
            delete itemproperty
        """
        try:
            self.item_storage.check_if_item_property_exists(item_property_id=item_property_id)
        except custom_exceptions.ItemPropertyDoesNotExistException:
            self.item_presenter.raise_exception_for_item_property_does_not_exist()

        self.item_storage.delete_item_property(item_property_id=item_property_id)

        self.item_presenter.get_response_for_delete_item_property()

    
    def update_item_property(self, item_property_id:int, value:str):

        """ELP
            check if itemproperty exists
            update item property value
        """

        try:
            self.item_storage.check_if_item_property_exists(item_property_id=item_property_id)
        except custom_exceptions.ItemPropertyDoesNotExistException:
            self.item_presenter.raise_exception_for_item_property_does_not_exist()

        self.item_storage.update_item_property(item_property_id=item_property_id, value=value)

        return self.item_presenter.get_response_for_update_item_property()

    def add_view_to_item(self, user_id:str, item_id:int):

        """ELP
            add view to item
        """
        self.item_storage.add_view_to_item(user_id=user_id,item_id=item_id)