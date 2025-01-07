from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import WarrantyAlreadyExistsException, ItemDoesNotExistException, WarrantyDoesNotExistException

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
        except WarrantyAlreadyExistsException:
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
        except ItemDoesNotExistException:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_warranty_exists(warranty_id=warranty_id)
        except WarrantyDoesNotExistException:
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
