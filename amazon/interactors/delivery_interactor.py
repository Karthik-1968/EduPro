from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.exceptions import order_custom_exceptions

class DeliveryInteractor:

    def __init__(self, order_storage:OrderStorageInterface):
        
        self.order_storage = order_storage

    def create_delivery_availability(self, can_receive_on_saturday:str, can_receive_on_sunday:str, \
                                     order_presenter: OrderPresenterInterface):

        """ELP
            -check if delivery availability exists
            -create delivery aviailability
        """

        try:
            self.order_storage.check_if_delivery_availability_already_exists(can_receive_on_saturday=can_receive_on_saturday,\
                                                                can_receive__on_sunday=can_receive_on_sunday)
        except order_custom_exceptions.DeliveryAvailabilityAlreadyExistsException:
            order_presenter.raise_exception_for_delivery_availability_already_exists()
        
        delivery_availability_id = self.order_storage.create_delivery_availability(can_receive_on_saturday=can_receive_on_saturday,\
                                                                            can_receive__on_sunday=can_receive_on_sunday)

        return order_presenter.get_response_for_create_delivery_availability(delivery_availability_id=delivery_availability_id)
    

    def add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int, order_presenter: OrderPresenterInterface):

        """ELP
            -check if order exists
            -check if delivery availability exists
            -add delivery availability to order
        """

        self._check_if_input_data_is_correct_for_add_delivery_availability_to_order(order_id=order_id, \
                                                                            delivery_availability_id=delivery_availability_id, 
                                                                            order_presenter=order_presenter)

        self.order_storage.add_delivery_availability_to_order(order_id=order_id, delivery_availability_id=delivery_availability_id)

        return order_presenter.get_response_for_add_delivery_availability_to_order()
    
    def _check_if_input_data_is_correct_for_add_delivery_availability_to_order(self, order_id:int, delivery_availability_id:int, \
                                                                               order_presenter: OrderPresenterInterface):

        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except order_custom_exceptions.OrderDoesNotExistException:
            order_presenter.raise_exception_for_order_does_not_exist()

        try:
            self.order_storage.check_if_delivery_availability_exists(delivery_availability_id=delivery_availability_id)
        except order_custom_exceptions.DeliveryAvailabilityDoesNotExistException:
            order_presenter.raise_exception_for_delivery_availability_does_not_exist()


    def create_delivery_service(self, name:str, email:str, contact_number:str, order_presenter: OrderPresenterInterface):
        
        """ELP
            -check if delivery service exists
            -create delivery service
        """

        try:
            self.order_storage.check_if_delivery_service_already_exists(name=name)
        except order_custom_exceptions.DeliveryServiceAlreadyExistsException:
            order_presenter.raise_exception_for_delivery_service_already_exists()
        
        delivery_service_id = self.order_storage.create_delivery_service(name=name, email=email, contact_number=contact_number)

        return order_presenter.get_response_for_create_delivery_service(delivery_service_id=delivery_service_id)
    

    def add_delivery_service_to_order(self, order_id:int, delivery_service_id:int, order_presenter: OrderPresenterInterface):

        """ELP
            -check if order exists
            -check if delivery service exists
            -add delivery service to order
        """

        self._check_if_input_data_is_correct_for_add_delivery_service_to_order(order_id=order_id, \
                                                                            delivery_service_id=delivery_service_id, \
                                                                                order_presenter=order_presenter)

        self.order_storage.add_delivery_service_to_order(order_id=order_id, delivery_service_id=delivery_service_id)

        return order_presenter.get_response_for_add_delivery_service_to_order()
    
    def _check_if_input_data_is_correct_for_add_delivery_service_to_order(self, order_id:int, delivery_service_id:int, \
                                                                          order_presenter: OrderPresenterInterface):
        
        try:
            self.order_storage.check_if_order_exists(order_id=order_id)
        except order_custom_exceptions.OrderDoesNotExistException:
            order_presenter.raise_exception_for_order_does_not_exist()

        try:
            self.order_storage.check_if_delivery_service_exists(delivery_service_id=delivery_service_id)
        except order_custom_exceptions.DeliveryServiceDoesNotExistException:
            order_presenter.raise_exception_for_delivery_service_does_not_exist()