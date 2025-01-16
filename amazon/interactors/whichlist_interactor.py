from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions import custom_exceptions

class WhichListInteractor:

    def __init__(self, item_storage: ItemStorageInterface, item_presenter: ItemPresenterInterface, user_storage: UserStorageInterface, \
                 user_presenter: UserPresenterInterface):
        
        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.user_storage = user_storage
        self.user_presenter = user_presenter

    
    def create_whishlist_for_user_wrapper(self, user_id:str, name:str):

        try:
            whishlist_id = self.create_whishlist_for_user(user_id=user_id, name=name)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()
        except custom_exceptions.WhishlistAlreadyCreatedException:
            self.item_presenter.raise_exception_for_whishlist_already_created()
        else:
            return self.item_presenter.get_response_for_create_whishlist_for_user(whishlist_id=whishlist_id)

    def create_whishlist_for_user(self, user_id:str, name:str):

        """ELP
            -check if user exists
            -check if user already has whishlist
            -create whishlist for user
        """
        self._check_if_input_data_is_correct_for_create_whishlist_for_user(user_id=user_id)

        return self.item_storage.create_whishlist_for_user(user_id=user_id, name=name)
    
    def _check_if_input_data_is_correct_for_create_whishlist_for_user(self, user_id:str):

        self.user_storage.check_if_user_exists(user_id=user_id)

        self.item_storage.check_if_whishlist_already_created_for_user(user_id=user_id)


    def add_item_to_whishlist_wrapper(self, whishlist_id:int, item_id:int):
        
        try:
            self.add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id)
        except custom_exceptions.WhishlistDoesNotExistException:
            self.item_presenter.raise_exception_for_whishlist_does_not_exist()
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()
        except custom_exceptions.ItemPropertyDoesNotExistException:
            self.item_presenter.raise_exception_for_item_property_does_not_exist()
        else:
            return self.item_presenter.get_response_for_add_item_to_whishlist()

    def add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):
        
        """ELP
            -check if whishlist exists
            -check if item exists
            -check if item properties exists
            -add item to whishlist
        """

        self._check_if_input_data_is_correct_for_add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id, item_properties=item_properties)

        return self.item_storage.add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id, item_properties=item_properties)
    
    def _check_if_input_data_is_correct_for_add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):
        
        self.item_storage.check_if_whishlist_exists(whishlist_id=whishlist_id)

        self.item_storage.check_if_item_exists(item_id=item_id)

        self.item_storage.check_if_item_properties_exists(item_properties=item_properties)


    def delete_item_from_whishlist_by_item_id_wrapper(self, whishlist_id:int, item_id:int):
        
        try:
            self.delete_item_from_whishlist_by_item_id(whishlist_id=whishlist_id, item_id=item_id)
        except custom_exceptions.WhishlistDoesNotExistException:
            self.item_presenter.raise_exception_for_whishlist_does_not_exist()
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()
        except custom_exceptions.ItemDoesNotExistInWhishlistException:
            self.item_presenter.raise_exception_for_item_does_not_exist_in_whishlist()
        else:
            return self.item_presenter.get_response_for_delete_item_from_whishlist()

    def delete_item_from_whishlist_by_item_id(self, whishlist_id:int, item_id:int):
        
        """ELP
            -check if whishlist exists
            -check if item 
            -check if item is in whishlist
            -delete item from whishlist
        """

        self._check_if_input_data_is_correct_for_delete_item_from_whishlist_by_item_id(whishlist_id=whishlist_id, item_id=item_id)

        return self.item_storage.delete_item_from_whishlist(whishlist_id=whishlist_id, item_id=item_id)
    
    def _check_if_input_data_is_correct_for_delete_item_from_whishlist_by_item_id(self, whishlist_id:int, item_id:int):
        
        self.item_storage.check_if_whishlist_exists(whishlist_id=whishlist_id)

        self.item_storage.check_if_item_exists(item_id=item_id)

        self.item_storage.check_if_item_is_in_whishlist(whishlist_id=whishlist_id, item_id=item_id)


    def get_recommendations_for_user_wrapper(self, user_id:str):
        
        try:
            recommendations_dtos = self.get_recommendations_for_user(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()
        else:
            return self.item_presenter.get_response_for_get_recommendations_for_user(recommendations_dtos=recommendations_dtos)
        
    def get_recommendations_for_user(self, user_id:str):

        """ELP
            -check if user exists
            -get recommendations for user
        """
        self.user_storage.check_if_user_exists(user_id=user_id)

        return self.item_storage.get_recommendations_for_user(user_id=user_id)