from amazoon.interactors.storage_interfaces import storage_interface
from amazoon.interactors.presenter_interfaces import presenter_interface
from amazoon.exceptions.custom_exception import UserDoesNotExist, ItemDoesNotExist, AddressDoesNotExist

class OrderInteractor:

    def __int__(self, storage: storage_interface, presenter: presenter_interface):
        self.storage = storage
        self.presenter = presenter

    def create_order(self, user_id:str, item_id:int, address_id:int, status:str, delivery_date:str):

        """ELP
            validate_input_details
                -validate user_id
                -validate item_id
                -validate address_id
                -validate status
                -validate delivery_date
            check if user exists
            check if item exists
            check if address exists
            create_order
        """
        self.validate_input_details_for_create_order(user_id=user_id, item_id=item_id, address_id=address_id, status=status, \
        delivery_date=delivery_date)

        try:
            self.storage.check_if_user_exists(user_id=user_id)
        except UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()

        try:
            self.storage.check_if_item_exists(item_id=item_id)
        except ItemDoesNotExist:
            self.presenter.raise_exception_for_item_does_not_exist()

        try:
            self.storage.check_if_address_exists(address_id=address_id)
        except AddressDoesNotExist:
            self.presenter.raise_exception_for_address_does_not_exist()

        order_id = self.storage.create_order(user_id=user_id, item_id=item_id, address_id=address_id, status=status,\
         delivery_date=delivery_date)

        return self.presenter.get_response_for_create_order(order_id=order_id)

    def validate_input_details_for_create_order(self, user_id:str, item_id:int, address_id:int, status:str, delivery_date:str):
        
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