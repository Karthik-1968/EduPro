from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemAlreadyExists, CategoryDoesNotExist, ItemDoesNotExist, PropertyAlreadyExists,\
 PropertyDoesNotExist, PropertyAlreadyAddedToItem, ItemPropertyDoesNotExist

class ItemInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_item(self, item_name:str, category_id:int, price:float):
        
        """ELP
            validate_input_details
                -validate item_name
                -validate category_id
                -validate price
            check if item already exists
            create_item
        """
        self.validate_input_details_for_create_item(item_name=item_name, category_id=category_id, price=price)

        try:
            self.storage.check_if_item_already_exists(item_name=item_name)
        except ItemAlreadyExists:
            self.presenter.raise_exception_for_item_already_exists()

        item_id = self.storage.create_item(item_name=item_name, category_id=category_id, price=price)

        return self.presenter.get_response_for_create_item(item_id=item_id)

    def validate_input_details_for_create_item(self, item_name:str, category_id:int, price:float):
        
        item_name_not_present = not item_name
        if item_name_not_present:
            self.presenter.raise_exception_for_missing_item_name()

        category_id_not_present = not category_id
        if category_id_not_present:
            self.presenter.raise_exception_for_missing_category_id()

        price_not_present = not price
        if price_not_present:
            self.presenter.raise_exception_for_missing_price()

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
        except CategoryDoesNotExist:
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
        except PropertyAlreadyExists:
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

        self.validate_input_details_for_add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        self.check_if_input_data_is_correct_for_add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        itemproperty_id = self.storage.add_property_to_item(item_id=item_id, property_id=property_id, value=value)

        return self.presenter.get_response_for_add_property_to_item(itemproperty_id=itemproperty_id)

    def validate_input_details_for_add_property_to_item(self, item_id:int, property_id:int, value:str):

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        property_id_not_present = not property_id
        if property_id_not_present:
            self.presenter.raise_exception_for_missing_property_id()

        value_not_present = not value
        if value_not_present:
            self.presenter.raise_exception_for_missing_value()

    def check_if_input_data_is_correct_for_add_property_to_item(self, item_id:int, property_id:int, value:str):

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExist:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_property_exists(property_id=property_id)
        except PropertyDoesNotExist:
            self.presenter.raise_exception_for_property_does_not_exist()

        try:
            self.storage.check_if_property_already_added_to_item(item_id=item_id, property_id=property_id, value=value)
        except PropertyAlreadyAddedToItem:
            self.presenter.raise_exception_for_property_already_added_to_item()


    def delete_item_property(self, itemproperty_id:int):

        """ELP
            validate itemproperty_id
            check if itemproperty exists
            delete itemproperty
        """

        itemproperty_id_not_present = not itemproperty_id
        if itemproperty_id_not_present:
            self.presenter.raise_exception_for_missing_item_property_id()

        try:
            self.storage.check_if_item_property_exists(itemproperty_id=itemproperty_id)
        except ItemPropertyDoesNotExist:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        self.storage.delete_item_property(itemproperty_id=itemproperty_id)

        self.presenter.get_response_for_delete_item_property()

    
    def update_item_property(self,itemproperty_id:int, value:str):

        """ELP
            -validate input details
                -validate itemproperty_id
                -validate value
            check if itemproperty exists
            update item property value
        """

        self.validate_input_details_for_update_item_property(itemproperty_id=itemproperty_id, value=value)

        try:
            self.storage.check_if_item_property_exists(itemproperty_id=itemproperty_id)
        except ItemPropertyDoesNotExist:
            self.presenter.raise_exception_for_item_property_does_not_exist()

        self.storage.update_item_property(itemproperty_id=itemproperty_id, value=value)

        return self.presenter.get_response_for_update_item_property()

    def validate_input_details_for_update_item_property(self,itemproperty_id:int, value:str):

        itemproperty_id_not_present = not itemproperty_id
        if itemproperty_id_not_present:
            self.presenter.raise_exception_for_missing_item_property_id()

        value_not_present = not value
        if value_not_present:
            self.presenter.raise_exception_for_missing_value()
