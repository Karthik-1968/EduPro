from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions

class ItemWarrentyInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):

        self.storage = storage
        self.presenter = presenter

    
    def create_warranty(self, warranty_name:str, warranty_amount:float, number_of_months:int):

        """ELP
            -validate input details
                -validate warranty_name
                -validate warranty_amount
                -validate number_of_months
            -check if warranty already exists
            -create warranty
        """

        self._validate_input_data_for_create_warranty(warranty_name=warranty_name, warranty_amount=warranty_amount, \
                                                      number_of_months=number_of_months)
        
        try:
            self.storage.check_if_warranty_already_exists(warranty_name=warranty_name, warranty_amount=warranty_amount, \
                                                          number_of_months=number_of_months)
        except custom_exceptions.WarrantyAlreadyExistsException:
            self.presenter.raise_exception_for_warrenty_already_exists()

        warranty_id = self.storage.create_warrenty(warranty_name=warranty_name, warranty_amount=warranty_amount, \
                                                          number_of_months=number_of_months)
        
        return self.presenter.get_response_for_create_warranty(warranty_id = warranty_id)
        
    def _validate_input_data_for_create_warranty(self, warranty_name:str, warranty_amount:float, number_of_months:int):

        warranty_name_not_present = not warranty_name
        if warranty_name_not_present:
            self.presenter.raise_exception_for_missing_warranty_name()

        warranty_amount_not_present = not warranty_amount
        if warranty_amount_not_present:
            self.presenter.raise_exception_for_missing_warranty_amount()

        number_of_months_not_present = not number_of_months
        if number_of_months_not_present:
            self.presenter.raise_exception_for_missing_number_of_months()

    
    def add_warranty_to_item(self, item_id:int, warranty_id:int):

        """ELP
            -validate input details
                -validate item_id
                -validate warranty_id
            -check if item exits
            -check if warranty exists
            -add warranty to item
        """
        self._validate_input_details_for_add_warranty_to_item(item_id=item_id, warranty_id=warranty_id)

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except custom_exceptions.ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_warranty_exists(warranty_id=warranty_id)
        except custom_exceptions.WarrantyDoesNotExistException:
            self.presenter.raise_exception_for_warranty_does_not_exists()

        item_warranty_id = self.storage.add_warranty_to_item(item_id=item_id, warranty_id=warranty_id)

        return self.presenter.get_response_for_add_warranty_to_items(item_warranty_id = item_warranty_id)
    
    def _validate_input_details_for_add_warranty_to_item(self, item_id:int, warranty_id:int):

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        warranty_id_not_present = not warranty_id
        if warranty_id_not_present:
            self.presenter.raise_exception_for_missing_warranty_id()

    
    def add_item_warranty_to_order(self, order_id:int, item_warranty_id:int):

        """ELP
            -check if order exists
            -check if item warranty exists
            -check if warranty is associated with the item
            -check if warranty is already associated with the order
            -add item warranty to order
        """
        self._check_if_input_data_is_correct_for_add_warranty_to_order(order_id=order_id, item_warranty_id=item_warranty_id)

        self.storage.add_item_warranty_to_order(order_id=order_id, item_warranty_id=item_warranty_id)

        return self.presenter.get_response_for_add_item_warranty_to_order()

    def _check_if_input_data_is_correct_for_add_warranty_to_order(self, order_id:int, item_warranty_id:int):

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_item_warranty_exists(item_warranty_id=item_warranty_id)
        except custom_exceptions.ItemWarrantyDoesNotExistException:
            self.presenter.raise_exception_for_item_warranty_does_not_exist()

        try:
            self.storage.check_if_warranty_is_associated_with_item(item_warranty_id=item_warranty_id, order_id=order_id)
        except custom_exceptions.WarrantyIsNotAssociatedWithItemException:
            self.presenter.raise_exception_for_item_warranty_is_not_associated_with_item()

        try:
            self.storage.check_if_warranty_is_already_associated_with_order(item_warranty_id=item_warranty_id, order_id=order_id)
        except custom_exceptions.WarrantyAlreadyAssociatedWithOrderException:
            self.presenter.raise_exception_for_warranty_already_associated_with_order()
