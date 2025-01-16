from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.storage_interfaces.item_offer_storage_interface import ItemOfferStorageInterface
from amazon.interactors.presenter_interfaces.item_offer_presenter_interface import ItemOfferPresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.dtos import ItemsCartDTO

class ItemsCartInteractor:

    def __init__(self, item_storage: ItemStorageInterface, user_storage: UserStorageInterface, item_offer_storage: ItemOfferStorageInterface):
        
        self.item_storage = item_storage
        self.user_storage = user_storage
        self.item_offer_storage = item_offer_storage

    def create_cart(self, user_id:str, name:str, item_presenter: ItemPresenterInterface, user_presenter: UserPresenterInterface):

        """ELP
            -check if user exists
            -check if user already has cart
            -create cart to user
        """
        self._check_if_input_data_is_correct_for_create_items_cart(user_id=user_id, user_presenter=user_presenter, \
                                                                   item_presenter=item_presenter)

        cart_id = self.item_storage.create_cart(user_id=user_id, name=name)

        return item_presenter.get_response_for_create_cart(cart_id=cart_id)

    def _check_if_input_data_is_correct_for_create_items_cart(self, user_id:str, user_presenter: UserPresenterInterface, \
                                                              item_presenter: ItemPresenterInterface):

        try:
            self.user_storage.check_if_user_exists(user_id=user_id)
        except custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()

        try:
            self.item_storage.check_if_cart_already_created_for_user(user_id=user_id)
        except custom_exceptions.CartAlreadyCreatedException:
            item_presenter.raise_exception_for_cart_already_created()


    def add_item_to_cart(self, itemscart_dto:ItemsCartDTO, item_presenter: ItemPresenterInterface, item_offer_presenter: ItemOfferPresenterInterface):

        """ELP
            -check if cart exists
            -check if item exists
            -add item to cart
        """
        self._check_if_input_data_for_cart_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter)

        self._check_if_input_data_for_item_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter)

        self._check_if_input_data_for_item_properties_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto, \
                                                                                      item_presenter=item_presenter)

        self._check_if_input_data_for_item_warranty_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto, \
                                                                                    item_presenter=item_presenter)

        self._check_if_input_data_for_item_exchange_property_is_correct_for_add_item_to_cart(itemscart_dto=itemscart_dto, \
                                                                                             item_offer_presenter=item_offer_presenter)

        self.item_storage.add_item_to_cart(itemscart_dto=itemscart_dto)

        return item_presenter.get_response_for_add_item_to_cart()

    def _check_if_input_data_for_cart_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO, item_presenter: ItemPresenterInterface):

        try:
            self.item_storage.check_if_cart_exists(cart_id=itemscart_dto.cart_id)
        except custom_exceptions.CartDoesNotExistException:
            item_presenter.raise_exception_for_cart_does_not_exist()

    def _check_if_input_data_for_item_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO, item_presenter: ItemPresenterInterface):

        try:
            self.item_storage.check_if_item_exists(item_id=itemscart_dto.item_id)
        except custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero(item_id=itemscart_dto.item_id)
        except custom_exceptions.OutOfStockException:
            item_presenter.raise_exception_for_out_of_stock()

    def _check_if_input_data_for_item_properties_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO, \
                                                                                 item_presenter: ItemPresenterInterface):

        try:
            self.item_storage.check_if_item_properties_exists(item_properties=itemscart_dto.item_properties)
        except custom_exceptions.ItemPropertyDoesNotExistException:
            item_presenter.raise_exception_for_item_property_does_not_exist()

        try:
            self.item_storage.check_if_item_properties_belong_to_item(item_id=itemscart_dto.item_id, \
                                                                      item_properties=itemscart_dto.item_properties)
        except custom_exceptions.ItemPropertyDoesNotBelongToItemException:
            item_presenter.raise_exception_for_item_property_does_not_belong_to_item()

    def _check_if_input_data_for_item_warranty_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO, \
                                                                               item_presenter: ItemPresenterInterface):

        if itemscart_dto.item_warranty_id is not None:
            try:
                self.item_storage.check_if_item_warranty_exists(item_warranty_id=itemscart_dto.item_warranty_id)
            except custom_exceptions.ItemWarrantyDoesNotExistException:
                item_presenter.raise_exception_for_item_warranty_does_not_exist()

            try:
                self.item_storage.check_if_warranty_is_associated_with_item(item_id=itemscart_dto.item_id, item_warranty_id=itemscart_dto.item_warranty_id)
            except custom_exceptions.WarrantyIsNotAssociatedWithItemException:
                item_presenter.raise_exception_for_item_warranty_is_not_associated_with_item()
    
    def _check_if_input_data_for_item_exchange_property_is_correct_for_add_item_to_cart(self, itemscart_dto:ItemsCartDTO, \
                                                                                         item_offer_presenter: ItemOfferPresenterInterface):

        if itemscart_dto.item_exchange_properties is not None:
            try:
                self.item_offer_storage.check_if_item_exchange_properties_exists(item_exchange_property_ids=itemscart_dto.item_exchange_properties)
            except custom_exceptions.ItemExchangePropertyDoesNotExistException:
                item_offer_presenter.raise_exception_for_item_exchange_property_does_not_exist()

            try:
                self.item_offer_storage.check_if_exchange_properties_are_associated_with_item_in_order(item_id=itemscart_dto.item_id, \
                                                            item_exchange_property_ids=itemscart_dto.item_exchange_properties)
            except custom_exceptions.ExchangePropertiesAreNotAssociatedWithItemInOrderException:
                item_offer_presenter.raise_exception_for_exchange_properties_are_not_associated_with_item_in_order()
    

    def delete_item_from_cart_by_item_id(self, cart_id:int, item_id:int, item_presenter: ItemPresenterInterface):

        """ELP
            -check if cart exists
            -check if item exists
            -check if item is in cart
            -delete item from cart
        """

        self._check_if_input_data_is_correct_for_delete_item_from_cart_by_item_id(cart_id=cart_id, item_id=item_id,\
                                                                                   item_presenter=item_presenter)

        self.item_storage.delete_item_from_cart(cart_id=cart_id, item_id=item_id)

        return item_presenter.get_response_for_delete_item_from_cart()
    
    def _check_if_input_data_is_correct_for_delete_item_from_cart_by_item_id(self, cart_id:int, item_id:int, \
                                                                             item_presenter: ItemPresenterInterface):

        try:
            self.item_storage.check_if_cart_exists(cart_id=cart_id)
        except custom_exceptions.CartDoesNotExistException:
            item_presenter.raise_exception_for_cart_does_not_exist()

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_item_is_in_cart(cart_id=cart_id, item_id=item_id)
        except custom_exceptions.ItemDoesNotExistInCartException:
            item_presenter.raise_exception_for_item_does_not_exist_in_cart()