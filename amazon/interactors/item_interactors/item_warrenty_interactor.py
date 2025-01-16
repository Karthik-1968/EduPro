from amazon.interactors.storage_interfaces.item_storage_interface import ItemStorageInterface
from amazon.interactors.presenter_interfaces.item_presenter_interface import ItemPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.exceptions import custom_exceptions

class ItemWarrentyInteractor:

    def __init__(self, order_storage:OrderStorageInterface, order_presenter:OrderPresenterInterface, \
                 item_storage: ItemStorageInterface, item_presenter: ItemPresenterInterface):

        self.order_storage = order_storage
        self.order_presenter = order_presenter
        self.item_storage = item_storage
        self.item_presenter = item_presenter

    
    def create_warranty(self, warranty_name:str, warranty_amount:float, number_of_months:int):

        """ELP
            -check if warranty already exists
            -create warranty
        """
        try:
            self.item_storage.check_if_warranty_already_exists(warranty_name=warranty_name, warranty_amount=warranty_amount, \
                                                          number_of_months=number_of_months)
        except custom_exceptions.WarrantyAlreadyExistsException:
            self.item_presenter.raise_exception_for_warrenty_already_exists()

        warranty_id = self.item_storage.create_warrenty(warranty_name=warranty_name, warranty_amount=warranty_amount, \
                                                          number_of_months=number_of_months)
        
        return self.item_presenter.get_response_for_create_warranty(warranty_id = warranty_id)

    
    def add_warranty_to_item(self, item_id:int, warranty_id:int):

        """ELP
            -check if item exits
            -check if warranty exists
            -add warranty to item
        """
        try:
            self.item_storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.item_presenter.raise_exception_for_item_does_not_exist()

        try:
            self.item_storage.check_if_warranty_exists(warranty_id=warranty_id)
        except custom_exceptions.WarrantyDoesNotExistException:
            self.item_presenter.raise_exception_for_warranty_does_not_exists()

        item_warranty_id = self.item_storage.add_warranty_to_item(item_id=item_id, warranty_id=warranty_id)

        return self.item_presenter.get_response_for_add_warranty_to_items(item_warranty_id = item_warranty_id)

    
    def add_item_warranty_to_order(self, order_id:int, item_warranty_id:int):

        """ELP
            -check if order exists
            -check if item warranty exists
            -check if warranty is associated with the item
            -check if warranty is already associated with the order
            -add item warranty to order
        """
        self._check_if_input_data_is_correct_for_add_warranty_to_order(order_id=order_id, item_warranty_id=item_warranty_id)

        self.item_storage.add_item_warranty_to_order(order_id=order_id, item_warranty_id=item_warranty_id)

        return self.item_presenter.get_response_for_add_item_warranty_to_order()

    def _check_if_input_data_is_correct_for_add_warranty_to_order(self, order_id:int, item_warranty_id:int):

        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.order_presenter.raise_exception_for_order_does_not_exist()

        try:
            self.item_storage.check_if_item_warranty_exists(item_warranty_id=item_warranty_id)
        except custom_exceptions.ItemWarrantyDoesNotExistException:
            self.item_presenter.raise_exception_for_item_warranty_does_not_exist()

        try:
            self.item_storage.check_if_warranty_is_associated_with_item(item_warranty_id=item_warranty_id, order_id=order_id)
        except custom_exceptions.WarrantyIsNotAssociatedWithItemException:
            self.item_presenter.raise_exception_for_item_warranty_is_not_associated_with_item()

        try:
            self.item_storage.check_if_warranty_is_already_associated_with_order(item_warranty_id=item_warranty_id, order_id=order_id)
        except custom_exceptions.WarrantyAlreadyAssociatedWithOrderException:
            self.item_presenter.raise_exception_for_warranty_already_associated_with_order()
