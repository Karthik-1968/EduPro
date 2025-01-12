from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import ItemsCartDTO

class ItemsCartInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_cart(self, user_id:str, name:str):

        """ELP
            -check if user exists
            -check if user already has cart
            -create cart to user
        """
        self._check_if_input_data_is_correct_for_create_items_cart(user_id=user_id)

        cart_id = self.storage.create_cart(user_id=user_id, name=name)

        return self.presenter.get_response_for_create_cart(cart_id=cart_id)

    def _check_if_input_data_is_correct_for_create_items_cart(self, user_id:str):

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_cart_already_created_for_user(user_id=user_id)
        except custom_exceptions.CartAlreadyCreatedException:
            self.presenter.raise_exception_for_cart_already_created()


    def add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        """ELP
            -check if cart exists
            -check if item exists
            -add item to cart
        """
        self._check_if_input_data_for_cart_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self._check_if_input_data_for_item_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self._check_if_input_data_for_item_properties_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self._check_if_input_data_for_item_warranty_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self._check_if_input_data_for_item_exchange_property_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto)

        self.storage.add_item_to_cart(itemscart_dto=itemscart_dto)

        return self.presenter.get_response_for_add_item_to_cart()

    def _check_if_input_data_for_cart_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        try:
            self.storage.check_if_cart_exists(cart_id=itemscart_dto.cart_id)
        except custom_exceptions.CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

    def _check_if_input_data_for_item_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        try:
            self.storage.check_if_item_exists(item_id=itemscart_dto.item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

    def _check_if_input_data_for_item_properties_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        try:
            self.storage.check_if_item_properties_exists(item_properties=itemscart_dto.item_properties)
        except custom_exceptions.ItemPropertyDoesNotExistException:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        try:
            self.storage.check_if_item_properties_belong_to_item(item_id=itemscart_dto.item_id, item_properties=itemscart_dto.item_properties)
        except custom_exceptions.ItemPropertyDoesNotBelongToItemException:
            self.presenter.raise_exception_for_item_property_does_not_belong_to_item()

    def _check_if_input_data_for_item_warranty_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        if itemscart_dto.item_warranty_id is not None:
            try:
                self.storage.check_if_item_warranty_exists(item_warranty_id=itemscart_dto.item_warranty_id)
            except custom_exceptions.ItemWarrantyDoesNotExistException:
                self.presenter.raise_exception_for_item_warranty_does_not_exist()

            try:
                self.storage.check_if_warranty_is_associated_with_item(item_id=itemscart_dto.item_id, item_warranty_id=itemscart_dto.item_warranty_id)
            except custom_exceptions.WarrantyIsNotAssociatedWithItemException:
                self.presenter.raise_exception_for_item_warranty_is_not_associated_with_item()
    
    def _check_if_input_data_for_item_exchange_property_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO):

        if itemscart_dto.item_exchange_property_ids is not None:
            try:
                self.storage.check_if_item_exchange_properties_exists(item_exchange_property_ids=itemscart_dto.item_exchange_property_ids)
            except custom_exceptions.ItemExchangePropertyDoesNotExistException:
                self.presenter.raise_exception_for_item_exchange_property_does_not_exist()

            try:
                self.storage.check_if_exchange_properties_are_associated_with_item_in_order(item_id=itemscart_dto.item_id, \
                                                            item_exchange_property_ids=itemscart_dto.item_exchange_property_ids)
            except custom_exceptions.ExchangePropertiesAreNotAssociatedWithItemInOrderException:
                self.presenter.raise_exception_for_exchange_properties_are_not_associated_with_item_in_order()
    

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
        except custom_exceptions.CartDoesNotExistException:
            self.presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_item_is_in_cart(cart_id=cart_id, item_id=item_id)
        except custom_exceptions.ItemDoesNotExistInCartException:
            self.presenter.raise_exception_for_item_does_not_exist_in_cart()