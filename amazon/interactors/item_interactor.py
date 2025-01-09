from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import ItemAlreadyExistsException, CategoryDoesNotExistException, ItemDoesNotExistException, \
    PropertyAlreadyExistsException, PropertyDoesNotExistException, PropertyAlreadyAddedToItemException, \
        ItemPropertyDoesNotExistException, UserDoesNotExistException
from amazon.interactors.storage_interfaces.storage_interface import ItemDTO

class ItemInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_item(self, item_name:str, category_id:int, price:float, number_of_left_in_stock:int, number_of_purchases_in_last_month:int):
        
        """ELP
            validate_input_details
                -validate item_name
                -validate category_id
                -validate price
                -number of left in stock
            check if item already exists
            create_item
        """
        item_dto = ItemDTO(item_name=item_name, category_id=category_id, price=price, number_of_left_in_stock=number_of_left_in_stock, \
                           number_of_purchases_in_last_month=number_of_purchases_in_last_month)
        
        self._validate_input_details_for_create_item(item_dto=item_dto)
        
        try:
            self.storage.check_if_category_exists(category_id=category_id)
        except CategoryDoesNotExistException:
            self.presenter.raise_exception_for_category_does_not_exist()

        try:
            self.storage.check_if_item_already_exists(item_name=item_name)
        except ItemAlreadyExistsException:
            self.presenter.raise_exception_for_item_already_exists()

        item_id = self.storage.create_item(item_dto=item_dto)

        return self.presenter.get_response_for_create_item(item_id=item_id)

    def _validate_input_details_for_create_item(self, item_dto:ItemDTO):
        
        item_name_not_present = not item_dto.item_name
        if item_name_not_present:
            self.presenter.raise_exception_for_missing_item_name()

        category_id_not_present = not item_dto.category_id
        if category_id_not_present:
            self.presenter.raise_exception_for_missing_category_id()

        price_not_present = not item_dto.price
        if price_not_present:
            self.presenter.raise_exception_for_missing_price()

        number_of_left_in_stock_not_present = not item_dto.number_of_left_in_stock
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