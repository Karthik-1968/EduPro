from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.whichlist_interactor import WhichListInteractor


class ItemPerformanceInteractor:
    
    def __init__(self, item_storage: ItemStorageInterface, item_presenter: ItemPresenterInterface, user_storage: UserStorageInterface, \
                 user_presenter: UserPresenterInterface):
        
        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.user_storage = user_storage
        self.user_presenter = user_presenter


    def get_list_best_selling_items_wrapper(self):
        
        best_selling_items_dtos = self.get_list_best_selling_items()

        return self.item_presenter.get_response_for_list_best_selling_items(best_selling_items_dtos=best_selling_items_dtos)

    def get_list_best_selling_items(self):

        """ELP
            -get list of best selling items
        """

        return self.item_storage.get_list_best_selling_items()

    
    def get_list_of_top_rated_items_wrapper(self):
        
        top_rated_items_dtos = self.get_list_of_top_rated_items()

        return self.item_presenter.get_response_for_list_of_top_rated_items(top_rated_items_dtos=top_rated_items_dtos)
    
    def get_list_of_top_rated_items(self):
        
        """ELP
            -get list of top rated items
        """
        return self.item_storage.get_list_of_top_rated_items()
    

    def get_recently_viewed_item_by_user_wrapper(self, user_id:str):
        
        try:
            recently_viewed_item = self.get_recently_viewed_item_by_user(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()
        except custom_exceptions.UserHasNotViewedAnyItemException:
            self.item_presenter.raise_exception_for_user_has_not_viewed_any_item()
        else:
            return self.item_presenter.get_response_for_recently_viewed_item_by_user(recently_viewed_item=recently_viewed_item)

    def get_recently_viewed_item_by_user(self, user_id:str):
        
        """ELP
            -check if user exists
            -check if user has recently viewed item
            -get recently viewed item by user
        """

        self.user_storage.check_if_user_exists(user_id=user_id)

        self.item_storage.check_if_user_viewed_any_item(user_id=user_id)

        return self.item_storage.get_recently_viewed_item_by_user(user_id=user_id)
    

    def get_recommendations_for_multiple_users_wrapper(self, user_ids:list[str]):
        
        try:
            recommendations = self.get_recommendations_for_multiple_users(user_ids=user_ids)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()
        except custom_exceptions.UserHasNotViewedAnyItemException:
            self.item_presenter.raise_exception_for_user_has_not_viewed_any_item()
        else:
            return self.presenter.get_response_for_recommendations_for_multiple_users(recommendations=recommendations)
        
    
    def get_recommendations_for_multiple_users(self, user_ids:list[str]):
        
        """ELP
            -check if user exists
            -check if user has recently viewed item
            -get recommendations for multiple users
        """
        total_recommendations = []
        for user_id in user_ids:
            self.user_storage.check_if_user_exists(user_id=user_id)

            self.item_storage.check_if_user_viewed_any_item(user_id=user_id)

            recommendations = WhichListInteractor.get_recommendations_for_user(user_id=user_id)

            total_recommendations.extend(recommendations)

        return total_recommendations