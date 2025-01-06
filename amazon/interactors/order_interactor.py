from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions.custom_exceptions import UserDoesNotExist, ItemDoesNotExist, AddressDoesNotExist, ItemPropertyDoesNotExist,\
OrderDoesNotExist
from amazon.interactors.storage_interfaces.storage_interface import OrderDTO

class OrderInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_order(self, user_id:str, item_id:int, address_id:int, status:str, delivery_date:str, properties:list[int]):

        """ELP
            validate_input_details
                -validate user_id
                -validate item_id
                -validate address_id
                -validate status
                -validate delivery_date
                -validate properties
            check if user exists
            check if item exists
            check if address exists
            check if properties exists
            create_order
        """
        self.validate_input_details_for_create_order(user_id=user_id, item_id=item_id, address_id=address_id, status=status, \
        delivery_date=delivery_date, properties=properties)

        order_dto = OrderDTO(user_id=user_id, item_id=item_id, address_id=address_id, status=status, delivery_date=delivery_date,\
                             properties=properties)

        self.check_if_input_data_is_correct_for_create(order_dto = order_dto)

        order_id = self.storage.create_order(order_dto=order_dto)

        return self.presenter.get_response_for_create_order(order_id=order_id)

    def validate_input_details_for_create_order(self, user_id:str, item_id:int, address_id:int, status:str, delivery_date:str, \
    properties:list[int]):
        
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        address_id_not_present = not address_id
        if address_id_not_present:
            self.presenter.raise_exception_for_missing_address_id()

        status_not_present = not status
        if status_not_present:
            self.presenter.raise_exception_for_missing_status()

        delivery_date_not_present = not delivery_date
        if delivery_date_not_present:
            self.presenter.raise_exception_for_missing_delivery_date()

        properties_not_present = not properties
        if properties_not_present:
            self.presenter.raise_exception_for_missing_properties()
    
    def check_if_input_data_is_correct_for_create(self,order_dto:OrderDTO):

        try:
            self.storage.check_if_user_exists(user_id=order_dto.user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=order_dto.item_id)
        except ItemDoesNotExist:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=order_dto.address_id)
        except AddressDoesNotExist:
            self.presenter.raise_exception_for_address_does_not_exist()

        try:
            self.storage.check_if_item_properties_exists(properties=order_dto.properties)
        except ItemPropertyDoesNotExist:
            self.presenter.raise_exception_for_item_property_does_not_exist()




    def get_orders_of_user(self, user_id:str):
        """ELP
            validate user_id
            check if user exists
            get_orders_of_user
        """
        user_id_not_present = not user_id
        if user_id_not_present:
            self.presenter.raise_exception_for_missing_user_id()

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        order_dtos = self.storage.get_orders_of_user(user_id=user_id)

        return self.presenter.get_response_for_get_orders_of_user(order_dtos=order_dtos)

    

    def get_orders_of_item(self, item_id:int):

        """ELP
            validate item_id
            check if item exists
            get_orders_of_item
        """
        item_id_not_present = not item_id
        if item_id_not_present:
            self.presenter.raise_exception_for_missing_item_id()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExist:
            self.presenter.raise_exception_for_item_does_not_exist()

        order_dtos = self.storage.get_orders_of_item(item_id=item_id)

        return self.presenter.get_response_for_get_orders_of_item(order_dtos=order_dtos)

    
    def delete_order(self, order_id:int):

        """ELP
            validate order_id
            check if order exists
            delete_order
        """
        order_id_not_present = not order_id
        if order_id_not_present:
            self.presenter.raise_exception_for_missing_order_id()

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except OrderDoesNotExist:
            self.presenter.raise_exception_for_order_does_not_exist()

        self.storage.delete_order(order_id=order_id)

        return self.presenter.get_response_for_delete_order()