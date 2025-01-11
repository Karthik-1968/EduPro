from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions

class ItemRatingInterctor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def rate_an_item(self, item_id:int, user_id:str, rating:str):

        """ELP
            -check if item exists
            -check if user exsits
            -check if user already rated item
            -create item rating
        """

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_user_already_rated_item(item_id=item_id, user_id=user_id)
        except custom_exceptions.UserAlreadyRatedItemException:
            self.presenter.raise_exception_for_user_already_rated_item()

        item_rating_id = self.storage.rate_an_item(item_id=item_id, user_id=user_id, rating=rating)

        return self.presenter.get_response_for_rate_an_item(item_rating_id=item_rating_id)

    
    def get_ratings_of_an_item(self, item_id:int):

        """ELP
            -check if item exists
            -check if item has rating
            -get rating of item
        """

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_is_rated(item_id=item_id)
        except custom_exceptions.ItemIsNotRatedException:
            self.presenter.raise_exception_for_item_not_rated()

        rating_dtos = self.storage.get_ratings_of_an_item(item_id=item_id)

        return self.presenter.get_response_for_ratings_of_an_item(rating_dtos=rating_dtos)