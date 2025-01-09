from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemDoesNotExistException, \
        ItemPropertyDoesNotExistException, UserDoesNotExistException, CartAlreadyCreatedException, CartDoesNotExistException, \
            ItemWarrantyDoesNotExistException, ItemExchangePropertyDoesNotExistException, ItemDoesNotExistInCartException
from typing import Optional
from amazon.interactors.storage_interfaces.storage_interface import ItemsCartDTO

class ItemsCartInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

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
        itemscart_dto = ItemsCartDTO(cart_id=cart_id, item_id=item_id, item_warranty_id=item_warranty_id, \
                                     item_properties=item_properties, item_exchange_property_ids=item_exchange_property_ids)
        
        self._validate_input_details_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self._check_if_input_data_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self.storage.add_item_to_cart(itemscart_dto=itemscart_dto)

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

    def _check_if_input_data_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        try:
            self.storage.check_if_cart_exists(cart_id=itemscart_dto.cart_id)
        except CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=itemscart_dto.item_id)
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_properties_exists(item_properties=itemscart_dto.item_properties)
        except ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        if itemscart_dto.item_warranty_id is not None:
            try:
                self.storage.check_if_item_warranty_exists(item_warranty_id=itemscart_dto.item_warranty_id)
            except ItemWarrantyDoesNotExistException:
                self.presenter.raise_exception_for_item_warranty_does_not_exist()

        if itemscart_dto.item_exchange_property_ids is not None:
            try:
                self.storage.check_if_item_exchange_properties_exists(item_exchange_property_ids=itemscart_dto.item_exchange_property_ids)
            except ItemExchangePropertyDoesNotExistException:
                self.presenter.raise_exception_for_item_exchange_property_does_not_exist()
    

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