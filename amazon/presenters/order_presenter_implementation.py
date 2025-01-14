from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound
from amazon.constants import exception_messages

class OrderPresenterImplementation(OrderPresenterInterface):

    def get_response_for_create_order_for_item(self, order_id:int):

        return {
            "order_id":order_id
        }
    
    def raise_exception_for_order_does_not_exist(self):
        raise NotFound(*exception_messages.ORDER_DOES_NOT_EXIST)
    
    def get_response_for_create_order_for_cart(self, order_id:int):

        return {
            "order_id":order_id
        }
    
