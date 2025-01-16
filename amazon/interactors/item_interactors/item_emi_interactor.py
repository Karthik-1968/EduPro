from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.exceptions import custom_exceptions
from typing import Optional
from amazon.interactors.storage_interfaces.dtos import EmiDTO


class ItemEmiInteractor:

    def __init__(self, item_storage:ItemStorageInterface, item_presenter:ItemPresenterInterface, order_storage:OrderStorageInterface, \
                 order_presenter:OrderPresenterInterface):

        self.item_storage = item_storage
        self.item_presenter = item_presenter
        self.order_storage = order_storage
        self.order_presenter = order_presenter


    def create_debit_card_emi(self, emi_dto:EmiDTO):
        """ELP
            -check if emi exists
            create debit card emi
        """
        try:
            self.item_storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.item_presenter.raise_exception_for_emi_already_exists()

        emi_id = self.item_storage.create_debit_card_emi(emi_dto=emi_dto)

        return self.item_presenter.get_response_for_create_debit_card_emi(emi_id=emi_id)

    def create_no_cost_emi(self, emi_dto:EmiDTO):

        """ELP
            -check if emi exists
            -create no cost emi
        """
        try:
            self.item_storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.item_presenter.raise_exception_for_emi_already_exists()

        emi_id = self.item_storage.create_no_cost_emi(emi_dto=emi_dto)

        return self.item_presenter.get_response_for_create_no_cost_emi(emi_id=emi_id)


    def create_other_emi_type(self, emi_dto:EmiDTO):
        
        """ELP
            -check if emi exists
            -create other emi type
        """
        try:
            self.item_storage.check_if_emi_already_exists(emi_dto=emi_dto)
        except custom_exceptions.EmiAlreadyExistsException:
            self.item_presenter.raise_exception_for_emi_already_exists()

        emi_id = self.item_storage.create_other_emi_type(emi_dto=emi_dto)

        return self.item_presenter.get_response_for_create_other_emi_type(emi_id=emi_id)

    
    def add_emi_to_item(self, item_id:int, emi_id:int):

        """ELP
            -check if item exists
            -check if emi exists
            -add emi to item
        """
        self._check_if_given_input_data_is_correct(item_id=item_id, emi_id=emi_id)

        item_emi_id = self.item_storage.add_emi_to_item(item_id=item_id, emi_id=emi_id)

        return self.item_presenter.get_response_for_add_emi_to_item(item_emi_id=item_emi_id)

    def _check_if_given_input_data_is_correct(self, item_id:int, emi_id:int):

        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_emi_exists(emi_id=emi_id)
        except custom_exceptions.EmiDoesNotExistException:
            self.item_presenter.raise_exception_for_emi_does_not_exist()

    
    def add_item_emi_to_order(self, order_id:int, item_emi_id:int):

        """ELP
            -check if order exists
            -check if item emi exists
            -check if item emi is associated with item
            -check if item emi is not already added to order
            -add item emi to order
        """

        self._check_if_input_data_is_correct_for_add_item_emi_to_order(order_id=order_id, item_emi_id=item_emi_id)

        self.item_storage.add_item_emi_to_order(order_id=order_id, item_emi_id=item_emi_id)

        return self.item_presenter.get_response_for_add_item_emi_to_order()
    
    def _check_if_input_data_is_correct_for_add_item_emi_to_order(self, order_id:int, item_emi_id:int):

        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.order_presenter.raise_exception_for_order_does_not_exist()

        try:
            self.item_storage.check_if_item_emi_exists(item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiDoesNotExistException:
            self.item_presenter.raise_exception_for_item_emi_does_not_exist()

        try:
            self.item_storage.check_if_item_emi_is_associated_with_item(order_id=order_id, item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiIsNotAssociatedWithItemException:
            self.item_presenter.raise_exception_for_item_emi_is_not_associated_with_item()

        try:
            self.item_storage.check_if_item_emi_is_not_already_added_to_order(order_id=order_id, item_emi_id=item_emi_id)
        except custom_exceptions.ItemEmiAlreadyAddedToOrderException:
            self.item_presenter.raise_exception_for_item_emi_already_added_to_order()