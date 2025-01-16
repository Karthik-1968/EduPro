from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.exceptions import custom_exceptions

class ItemRatingInterctor:

    def __init__(self, user_storage: UserStorageInterface, user_presenter: UserPresenterInterface, item_storage: ItemStorageInterface, \
                 item_presenter: ItemPresenterInterface):

        self.user_storage = user_storage
        self.user_presenter = user_presenter
        self.item_storage = item_storage
        self.item_presenter = item_presenter

    def rate_an_item(self, item_id:int, user_id:str, rating:str):

        """ELP
            -check if item exists
            -check if user exsits
            -check if user already rated item
            -create item rating
        """

        self._check_if_input_data_is_correct_for_rate_an_item(item_id=item_id, user_id=user_id)

        item_rating_id = self.item_storage.rate_an_item(item_id=item_id, user_id=user_id, rating=rating)

        return self.item_presenter.get_response_for_rate_an_item(item_rating_id=item_rating_id)
    
    def _check_if_input_data_is_correct_for_rate_an_item(self, item_id:int, user_id:str):

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.user_storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.user_presenter.raise_exception_for_user_does_not_exist()

        try:
            self.item_storage.check_if_user_already_rated_item(item_id=item_id, user_id=user_id)
        except custom_exceptions.UserAlreadyRatedItemException:
            self.item_presenter.raise_exception_for_user_already_rated_item()

    
    def get_ratings_of_an_item(self, item_id:int):

        """ELP
            -check if item exists
            -check if item has rating
            -get rating of item
        """

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_item_is_rated(item_id=item_id)
        except custom_exceptions.ItemIsNotRatedException:
            self.item_presenter.raise_exception_for_item_not_rated()

        rating_dtos = self.item_storage.get_ratings_of_an_item(item_id=item_id)

        return self.item_presenter.get_response_for_ratings_of_an_item(rating_dtos=rating_dtos)