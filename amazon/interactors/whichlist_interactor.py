from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemDoesNotExistException, ItemPropertyDoesNotExistException, \
    UserDoesNotExistException, WhishlistAlreadyCreatedException, WhishlistDoesNotExistException, \
                    ItemDoesNotExistInWhishlistException

class WhichListInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    
    def create_whishlist_for_user_wrapper(self, user_id:str, name:str):

        try:
            whishlist_id = self.create_whishlist_for_user(user_id=user_id, name=name)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()
        except WhishlistAlreadyCreatedException:
            self.presenter.raise_exception_for_whishlist_already_created()
        else:
            return self.presenter.get_response_for_create_whishlist_for_user(whishlist_id=whishlist_id)

    def create_whishlist_for_user(self, user_id:str, name:str):

        """ELP
            -check if user exists
            -check if user already has whishlist
            -create whishlist for user
        """
        self._check_if_input_data_is_correct_for_create_whishlist_for_user(user_id=user_id)

        return self.storage.create_whishlist_for_user(user_id=user_id, name=name)
    
    def _check_if_input_data_is_correct_for_create_whishlist_for_user(self, user_id:str):

        self.storage.check_if_user_exists(user_id=user_id)

        self.storage.check_if_whishlist_already_created_for_user(user_id=user_id)


    def add_item_to_whishlist_wrapper(self, whishlist_id:int, item_id:int):
        
        try:
            self.add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id)
        except WhishlistDoesNotExistException:
            self.presenter.raise_exception_for_whishlist_does_not_exist()
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()
        else:
            return self.presenter.get_response_for_add_item_to_whishlist()

    def add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):
        
        """ELP
            -check if whishlist exists
            -check if item exists
            -check if item properties exists
            -add item to whishlist
        """

        self._check_if_input_data_is_correct_for_add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id, item_properties=item_properties)

        return self.storage.add_item_to_whishlist(whishlist_id=whishlist_id, item_id=item_id, item_properties=item_properties)
    
    def _check_if_input_data_is_correct_for_add_item_to_whishlist(self, whishlist_id:int, item_id:int, item_properties:list[int]):
        
        self.storage.check_if_whishlist_exists(whishlist_id=whishlist_id)

        self.storage.check_if_item_exists(item_id=item_id)

        self.storage.check_if_item_properties_exists(item_properties=item_properties)


    def delete_item_from_whishlist_by_item_id_wrapper(self, whishlist_id:int, item_id:int):
        
        try:
            self.delete_item_from_whishlist_by_item_id(whishlist_id=whishlist_id, item_id=item_id)
        except WhishlistDoesNotExistException:
            self.presenter.raise_exception_for_whishlist_does_not_exist()
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()
        except ItemDoesNotExistInWhishlistException:
            self.presenter.raise_exception_for_item_does_not_exist_in_whishlist()
        else:
            return self.presenter.get_response_for_delete_item_from_whishlist()

    def delete_item_from_whishlist_by_item_id(self, whishlist_id:int, item_id:int):
        
        """ELP
            -check if whishlist exists
            -check if item 
            -check if item is in whishlist
            -delete item from whishlist
        """

        self._check_if_input_data_is_correct_for_delete_item_from_whishlist_by_item_id(whishlist_id=whishlist_id, item_id=item_id)

        return self.storage.delete_item_from_whishlist(whishlist_id=whishlist_id, item_id=item_id)
    
    def _check_if_input_data_is_correct_for_delete_item_from_whishlist_by_item_id(self, whishlist_id:int, item_id:int):
        
        self.storage.check_if_whishlist_exists(whishlist_id=whishlist_id)

        self.storage.check_if_item_exists(item_id=item_id)

        self.storage.check_if_item_is_in_whishlist(whishlist_id=whishlist_id, item_id=item_id)


    def get_recommendations_for_user_wrapper(self, user_id:str):
        
        try:
            recommendations_dtos = self.get_recommendations_for_user(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()
        else:
            return self.presenter.get_response_for_get_recommendations_for_user(recommendations_dtos=recommendations_dtos)
        
    def get_recommendations_for_user(self, user_id:str):

        """ELP
            -check if user exists
            -get recommendations for user
        """
        self.storage.check_if_user_exists(user_id=user_id)

        return self.storage.get_recommendations_for_user(user_id=user_id)