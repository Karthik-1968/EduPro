from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemDoesNotExistException, ItemIsNotRatedException

class ItemRatingInterctor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_rating_for_item(self, item_id:int):

        """ELP
            -validate input details
                -validate item_id
            -check if item exists
            -create item rating
        """

        item_id_not_exist = not item_id
        if item_id_not_exist:
            self.presenter.raise_exception_for_missing_item_id()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        item_rating_id = self.storage.create_rating_for_item(item_id=item_id)

        return self.presenter.get_response_for_create_rating_for_item(item_rating_id=item_rating_id)
    
    
    def add_rating_to_item(self, item_id:int, rating:int):

        """ELP
            -validate input details
                -validate item_id
                -validate rating
            -check if item exists
            -add rating to item
        """

        self._validate_input_details_for_add_rating_to_item(item_id=item_id, rating=rating)

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        self.storage.add_rating_to_item(item_id=item_id, rating=rating)

        return self.presenter.get_response_for_add_rating_to_item()

    def _validate_input_details_for_add_rating_to_item(self, item_id:int, rating:int):

        item_id_not_exist = not item_id
        if item_id_not_exist:
            self.presenter.raise_exception_for_missing_item_id()

        rating_not_exist = not rating
        if rating_not_exist:
            self.presenter.raise_exception_for_missing_rating()

    
    def get_rating_of_item(self, item_id:int):

        """ELP
            -validate input details
                -validate item_id
            -check if item exists
            -check if item has rating
            -get rating of item
        """

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_is_rated(item_id=item_id)
        except ItemIsNotRatedException:
            self.presenter.raise_exception_for_item_not_rated()

        item_rating = self.storage.get_item_rating(item_id=item_id)

        return self.presenter.get_response_for_get_item_rating(item_rating=item_rating)