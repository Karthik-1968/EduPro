from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.item_offer_storage_interface import ItemOfferStorageInterface
from amazon.interactors.presenter_interfaces.item_offer_presenter_interface import ItemOfferPresenterInterface
from amazon.exceptions import custom_exceptions
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.interactors.item_interactors.items_cart_interactor import ItemsCartInteractor
from amazon.interactors.storage_interfaces.dtos import ItemsCartDTO
from mock import create_autospec
import pytest

class TestAddItemToCartInteractor:

    def setup_method(self):

        self.item_storage = create_autospec(ItemStorageInterface)
        self.user_storage = create_autospec(UserStorageInterface)
        self.item_offer_storage = create_autospec(ItemOfferStorageInterface)
        self.interactor = ItemsCartInteractor(item_storage=self.item_storage, user_storage=self.user_storage, \
                                              item_offer_storage=self.item_offer_storage)

    def test_if_item_does_not_exist_raises_exception(self):
        
        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.check_if_item_exists.side_effect = custom_exceptions.ItemDoesNotExistException
        item_presenter.raise_exception_for_item_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter, \
                                             item_offer_presenter=item_offer_presenter) 
            
        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=itemscart_dto.item_id)
        item_presenter.raise_exception_for_item_does_not_exist.assert_called_once()

    def test_if_cart_does_not_exist_raises_exception(self):

        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.check_if_cart_exists.side_effect = custom_exceptions.CartDoesNotExistException
        item_presenter.raise_exception_for_cart_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter,\
                                              item_offer_presenter=item_offer_presenter)
            
        self.item_storage.check_if_cart_exists.assert_called_once_with(cart_id=itemscart_dto.cart_id)
        item_presenter.raise_exception_for_cart_does_not_exist.assert_called_once()

    def test_if_number_of_stocks_less_than_zero_raises_exception(self):
        
        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.side_effect = custom_exceptions.OutOfStockException
        item_presenter.raise_exception_for_out_of_stock.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter, \
                                             item_offer_presenter=item_offer_presenter)
            
        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.assert_called_once_with(item_id=itemscart_dto.item_id)
        item_presenter.raise_exception_for_out_of_stock.assert_called_once()

    def test_if_item_properties_does_not_exist_raises_exception(self):

        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.check_if_item_properties_exists.side_effect = custom_exceptions.ItemPropertyDoesNotExistException
        item_presenter.raise_exception_for_item_property_does_not_exist.side_effect = NotFound

        with pytest.raises(NotFound):
            self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter, \
                                             item_offer_presenter=item_offer_presenter)
            
        self.item_storage.check_if_item_properties_exists.assert_called_once_with(item_properties=itemscart_dto.item_properties)
        item_presenter.raise_exception_for_item_property_does_not_exist.assert_called_once()

    def test_if_item_properties_does_not_belong_to_item_raises_exception(self):

        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.check_if_item_properties_belong_to_item.side_effect = custom_exceptions.ItemPropertyDoesNotBelongToItemException
        item_presenter.raise_exception_for_item_property_does_not_belong_to_item.side_effect = BadRequest

        with pytest.raises(BadRequest):
            self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter, \
                                             item_offer_presenter=item_offer_presenter)
            
        self.item_storage.check_if_item_properties_belong_to_item.assert_called_once_with(item_id=itemscart_dto.item_id, \
                                                                                          item_properties=itemscart_dto.item_properties)
        item_presenter.raise_exception_for_item_property_does_not_belong_to_item.assert_called_once()

    def test_add_item_to_cart(self):

        itemscart_dto = ItemsCartDTO(
                item_id = 1,
                cart_id = 1,
                item_properties = [1, 2],
                item_warranty_id = None,
                item_exchange_properties = None)

        item_presenter = create_autospec(ItemPresenterInterface)
        item_offer_presenter = create_autospec(ItemOfferPresenterInterface)

        self.item_storage.add_item_to_cart.return_value = None
        item_presenter.get_response_for_add_item_to_cart.return_value = None

        self.interactor.add_item_to_cart(itemscart_dto=itemscart_dto, item_presenter=item_presenter, \
                                         item_offer_presenter=item_offer_presenter)
        
        self.item_storage.check_if_item_exists.assert_called_once_with(item_id=itemscart_dto.item_id)
        self.item_storage.check_if_cart_exists.assert_called_once_with(cart_id=itemscart_dto.cart_id)
        self.item_storage.check_if_number_of_left_in_stock_is_greater_than_zero.assert_called_once_with(item_id=itemscart_dto.item_id)
        self.item_storage.check_if_item_properties_exists.assert_called_once_with(item_properties=itemscart_dto.item_properties)
        self.item_storage.check_if_item_properties_belong_to_item.assert_called_once_with(item_id=itemscart_dto.item_id, \
                                                                                            item_properties=itemscart_dto.item_properties)
        self.item_storage.add_item_to_cart.assert_called_once_with(itemscart_dto=itemscart_dto)
        item_presenter.get_response_for_add_item_to_cart.assert_called_once()