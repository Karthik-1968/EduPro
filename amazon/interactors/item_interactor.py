from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemAlreadyExistsException, CategoryDoesNotExistException, ItemDoesNotExistException, \
    PropertyAlreadyExistsException, PropertyDoesNotExistException, PropertyAlreadyAddedToItemException, \
        ItemPropertyDoesNotExistException, UserDoesNotExistException, CartAlreadyCreatedException, CartDoesNotExistException, \
            ItemIsNotRatedException, ItemWarrantyDoesNotExistException, ItemExchangePropertyDoesNotExistException, \
                ItemDoesNotExistInCartException
from typing import Optional

class ItemInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_item(self, item_name:str, category_id:int, price:float, number_of_left_in_stock:int):
        
        """ELP
            validate_input_details
                -validate item_name
                -validate category_id
                -validate price
                -number of left in stock
            check if item already exists
            create_item
        """
        self._validate_input_details_for_create_item(item_name=item_name, category_id=category_id, price=price, \
                                                     number_of_left_in_stock=number_of_left_in_stock)

        try:
            self.storage.check_if_item_already_exists(item_name=item_name)
        except ItemAlreadyExistsException:
            self.presenter.raise_exception_for_item_already_exists()

        item_id = self.storage.create_item(item_name=item_name, category_id=category_id, price=price,\
                                           number_of_left_in_stock=number_of_left_in_stock)

        return self.presenter.get_response_for_create_item(item_id=item_id)

    def _validate_input_details_for_create_item(self, item_name:str, category_id:int, price:float, number_of_left_in_stock:int):
        
        item_name_not_present = not item_name
        if item_name_not_present:
            self.presenter.raise_exception_for_missing_item_name()

        category_id_not_present = not category_id
        if category_id_not_present:
            self.presenter.raise_exception_for_missing_category_id()

        price_not_present = not price
        if price_not_present:
            self.presenter.raise_exception_for_missing_price()

        number_of_left_in_stock_not_present = not number_of_left_in_stock
        if number_of_left_in_stock_not_present:
            self.presenter.raise_exception_for_missing_number_of_left_in_stock()

    def get_item_details(self, item_id: str, user_id: str):

        """ELP
            -validate input details
                -validate user_id
                -validate item_id
            -check if user exists
            -check if item exists
            -get item details
        """
        self._validate_input_details_for_get_item_details(item_id=item_id, user_id=user_id)

        self._check_if_input_data_is_correct(item_id=item_id, user_id=user_id)

        self.add_view_to_item(user_id=user_id, item_id=item_id)

        item_dto = self.storage.get_item_details(item_id=item_id)

        return self.presenter.get_response_for_get_item_details(item_dto=item_dto)

    def _validate_input_details_for_get_item_details(self, item_id:int, user_id:str):

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

    def _check_if_input_data_is_correct(self, item_id:int, user_id:str):

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()


    def get_list_of_items(self):

        item_dtos = self.storage.get_list_of_items()

        return self.presenter.get_response_for_list_of_items(item_dtos=item_dtos)


    def get_list_of_items_by_category(self, category_id:int):

        """ELP
            validate_input_details
                -validate category_id
            check if category exists
            get_list_of_items_by_category
        """

        category_id_not_present = not category_id
        if category_id_not_present:
            self.presenter.raise_exception_for_missing_category_id()

        try:
            self.storage.check_if_category_exists(category_id=category_id)
        except CategoryDoesNotExistException:
            self.presenter.raise_exception_for_category_does_not_exist()

        item_dtos = self.storage.get_list_of_items_by_category(category_id=category_id)

        return self.presenter.get_response_for_list_of_items_by_category(item_dtos=item_dtos)

    def create_property(self, property_name:str):
        
        """ELP
            validate_input_details
                -validate property_name
            check if property already exists
            create_property
        """

        property_name_not_present = not property_name
        if property_name_not_present:
            self.presenter.raise_exception_for_missing_property_name()

        try:
            self.storage.check_if_property_already_exists(property_name=property_name)
        except PropertyAlreadyExistsException:
            self.presenter.raise_exception_for_property_already_exists()

        property_id = self.storage.create_property(property_name=property_name)

        return self.presenter.get_response_for_create_property(property_id=property_id)

    def add_property_to_item(self, item_id:int, property_id:int, value:str):

        """ELP
            validate_input_details
                -validate item_id
                -validate property_id
                -validate value
            check if item exists
            check if property exists
            check if property already added to item
            add_property_to_item
        """

        self._validate_input_details_for_add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        self._check_if_input_data_is_correct_for_add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        itemproperty_id = self.storage.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        return self.presenter.get_response_for_add_property_to_item(itemproperty_id=itemproperty_id)

    def _validate_input_details_for_add_property_to_item(self, item_id:int, property_id:int, value:str):

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        property_id_not_present = not property_id
        if property_id_not_present:
            self.presenter.raise_exception_for_missing_property_id()

        value_not_present = not value
        if value_not_present:
            self.presenter.raise_exception_for_missing_value()

    def _check_if_input_data_is_correct_for_add_property_to_item(self, item_id:int, property_id:int, value:str):

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_property_exists(property_id=property_id)
        except PropertyDoesNotExistException:
            self.presenter.raise_exception_for_property_does_not_exist()

        try:
            self.storage.check_if_property_already_added_to_item(item_id=item_id, property_id=property_id, value=value)
        except PropertyAlreadyAddedToItemException:
            self.presenter.raise_exception_for_property_already_added_to_item()


    def delete_item_property(self, item_property_id:int):

        """ELP
            validate itemproperty_id
            check if itemproperty exists
            delete itemproperty
        """

        item_property_id_not_present = not item_property_id
        if item_property_id_not_present:
            self.presenter.raise_exception_for_missing_item_property_id()

        try:
            self.storage.check_if_item_property_exists(item_property_id=item_property_id)
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        self.storage.delete_item_property(item_property_id=item_property_id)

        self.presenter.get_response_for_delete_item_property()

    
    def update_item_property(self, item_property_id:int, value:str):

        """ELP
            -validate input details
                -validate itemproperty_id
                -validate value
            check if itemproperty exists
            update item property value
        """

        self._validate_input_details_for_update_item_property(item_property_id=item_property_id, value=value)

        try:
            self.storage.check_if_item_property_exists(item_property_id=item_property_id)
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        self.storage.update_item_property(item_property_id=item_property_id, value=value)

        return self.presenter.get_response_for_update_item_property()

    def _validate_input_details_for_update_item_property(self,item_property_id:int, value:str):

        item_property_id_not_present = not item_property_id
        if item_property_id_not_present:
            self.presenter.raise_exception_for_missing_item_property_id()

        value_not_present = not value
        if value_not_present:
            self.presenter.raise_exception_for_missing_value()

    def add_view_to_item(self, user_id:str, item_id:int):

        """ELP
            add view to item
        """
        self.storage.add_view_to_item(user_id=user_id,item_id=item_id)

    def create_cart(self, user_id:str, name:str):

        """ELP
            -validate input details
                -validate user_id
                -validate name
            -check if user exists
            -check if user already has cart
            -create cart to user
        """

        self._validate_input_details_for_create_items_cart(user_id=user_id, name=name)

        self._check_if_input_data_is_correct_for_create_items_cart(user_id=user_id)

        cart_id = self.storage.create_cart(user_id=user_id, name=name)

        return self.presenter.get_response_for_create_cart(cart_id=cart_id)

    def _validate_input_details_for_create_items_cart(self, user_id:str, name:str):

        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        cart_name_not_present = not name
        if cart_name_not_present:
            self.presenter.raise_exception_for_missing_cart_name()

    def _check_if_input_data_is_correct_for_create_items_cart(self, user_id:str):

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_cart_already_created_for_user(user_id=user_id)
        except CartAlreadyCreatedException:
            self.presenter.raise_exception_for_cart_already_created()


    def add_item_to_cart(self, cart_id:int, item_id:int, item_warranty_id:Optional[int], item_exchange_property_ids:Optional[list[int]], item_properties:list[int]):

        """ELP
            -validate input details
                -validate cart_id
                -validate item_id
            -check if cart exists
            -check if item exists
            -add item to cart
        """

        self._validate_input_details_for_add_item_to_cart(cart_id=cart_id, item_id=item_id, item_properties=item_properties)

        self._check_if_input_data_is_correct_for_add_item_to_cart(cart_id=cart_id, item_id=item_id, item_warranty_id=item_warranty_id,\
                                                                item_exchange_property_ids=item_exchange_property_ids, item_properties=item_properties)

        self.storage.add_item_to_cart(cart_id=cart_id, item_id=item_id, item_warranty_id=item_warranty_id, \
                                                     item_properties=item_properties, item_exchange_property_ids=item_exchange_property_ids)

        return self.presenter.get_response_for_add_item_to_cart()

    def _validate_input_details_for_add_item_to_cart(self, cart_id:int, item_id:int, item_properties:list[int]):

        cart_id_not_present = not cart_id
        if cart_id_not_present:
            self.presenter.raise_exception_for_missing_cart_id()

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        properties_not_present = not item_properties
        if properties_not_present:
            self.presenter.raise_exception_for_missing_properties()

    def _check_if_input_data_is_correct_for_add_item_to_cart(self, cart_id:int, item_id:int, item_warranty_id:Optional[int], 
                                                             item_properties:list[int], item_exchange_property_ids:Optional[list[int]]):

        try:
            self.storage.check_if_cart_exists(cart_id=cart_id)
        except CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_properties_exists(item_properties=item_properties)
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        if item_warranty_id is not None:
            try:
                self.storage.check_if_item_warranty_exists(item_warranty_id=item_warranty_id)
            except ItemWarrantyDoesNotExistException:
                self.presenter.raise_exception_for_item_warranty_does_not_exist()

        if item_exchange_property_ids is not None:
            try:
                self.storage.check_if_item_exchange_properties_exists(item_exchange_property_ids=item_exchange_property_ids)
            except ItemExchangePropertyDoesNotExistException:
                self.presenter.raise_exception_for_item_exchange_property_does_not_exist()

    
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
    

    def delete_item_from_cart_by_item_id(self, cart_id:int, item_id:int):

        """ELP
            -check if cart exists
            -check if item exists
            -check if item is in cart
            -delete item from cart
        """

        self._check_if_input_data_is_correct_for_delete_item_from_cart_by_item_id(cart_id=cart_id, item_id=item_id)

        self.storage.delete_item_from_cart(cart_id=cart_id, item_id=item_id)

        return self.presenter.get_response_for_delete_item_from_cart()
    
    def _check_if_input_data_is_correct_for_delete_item_from_cart_by_item_id(self, cart_id:int, item_id:int):

        try:
            self.storage.check_if_cart_exists(cart_id=cart_id)
        except CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_is_in_cart(cart_id=cart_id, item_id=item_id)
        except ItemDoesNotExistInCartException:
            self.presenter.raise_exception_for_item_does_not_exist_in_cart()