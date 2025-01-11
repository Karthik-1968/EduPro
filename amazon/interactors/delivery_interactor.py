from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions

class DeliveryInteractor:

    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):
        
        self.storage = storage
        self.presenter = presenter

    def create_delivery_availability(self, can_receive_on_saturday:str, can_receive_on_sunday:str):

        """ELP
            -check if delivery availability exists
            -create delivery aviailability
        """

        try:
            self.storage.check_if_delivery_availability_already_exists(can_receive_on_saturday=can_receive_on_saturday,\
                                                                can_receive__on_sunday=can_receive_on_sunday)
        except custom_exceptions.DeliveryAvailabilityAlreadyExistsException:
            self.presenter.raise_exception_for_delivery_availability_already_exists()
        
        delivery_availability_id = self.storage.create_delivery_availability(can_receive_on_saturday=can_receive_on_saturday,\
                                                                            can_receive__on_sunday=can_receive_on_sunday)

        return self.presenter.get_response_for_create_delivery_availability(delivery_availability_id=delivery_availability_id)
    

    def add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int):

        """ELP
            -check if order exists
            -check if delivery availability exists
            -add delivery availability to order
        """

        self._check_if_input_data_is_correct_for_add_delivery_availability_to_order(order_id=order_id, \
                                                                            delivery_availability_id=delivery_availability_id)

        self.storage.add_delivery_availability_to_order(order_id=order_id, delivery_availability_id=delivery_availability_id)

        return self.presenter.get_response_for_add_delivery_availability_to_order()
    
    def _check_if_input_data_is_correct_for_add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int):

        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_delivery_availability_exists(delivery_availability_id=delivery_availability_id)
        except custom_exceptions.DeliveryAvailabilityDoesNotExistException:
            self.presenter.raise_exception_for_delivery_availability_does_not_exist()


    def create_delivery_service(self, name:str, email:str, contact_number:str):
        
        """ELP
            -check if delivery service exists
            -create delivery service
        """

        try:
            self.storage.check_if_delivery_service_already_exists(name=name)
        except custom_exceptions.DeliveryServiceAlreadyExistsException:
            self.presenter.raise_exception_for_delivery_service_already_exists()
        
        delivery_service_id = self.storage.create_delivery_service(name=name, email=email, contact_number=contact_number)

        return self.presenter.get_response_for_create_delivery_service(delivery_service_id=delivery_service_id)
    

    def add_delivery_service_to_order(self, order_id:int, delivery_service_id:int):

        """ELP
            -check if order exists
            -check if delivery service exists
            -add delivery service to order
        """

        self._check_if_input_data_is_correct_for_add_delivery_service_to_order(order_id=order_id, \
                                                                            delivery_service_id=delivery_service_id)

        self.storage.add_delivery_service_to_order(order_id=order_id, delivery_service_id=delivery_service_id)

        return self.presenter.get_response_for_add_delivery_service_to_order()
    
    def _check_if_input_data_is_correct_for_add_delivery_service_to_order(self, order_id:int, delivery_service_id:int):
        
        try:
            self.storage.check_if_order_exists(order_id=order_id)
        except custom_exceptions.OrderDoesNotExistException:
            self.presenter.raise_exception_for_order_does_not_exist()

        try:
            self.storage.check_if_delivery_service_exists(delivery_service_id=delivery_service_id)
        except custom_exceptions.DeliveryServiceDoesNotExistException:
            self.presenter.raise_exception_for_delivery_service_does_not_exist()