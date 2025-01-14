from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from amazon.constants import exception_messages

class PaymentPresenterImplementation(PaymentPresenterInterface):

    def get_response_for_create_card_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def raise_exception_for_payment_method_does_not_exist(self):
        raise NotFound(*exception_messages.PAYMENT_METHOD_DOES_NOT_EXIST)
    
    def get_response_for_create_netbanking_payment_method(self, paymentmethod_id:int):
        
        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def get_response_for_create_upi_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def get_response_for_create_cash_on_delivery_payment_method(self, paymentmethod_id:int):

        return {
            "paymentmethod_id": paymentmethod_id
        }
    
    def raise_exception_for_card_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.CARD_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_netbanking_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.NETBANKING_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_upi_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.UPI_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def raise_exception_for_cash_on_delivery_payment_method_already_exists(self):
        raise BadRequest(*exception_messages.CASH_ON_DELIVERY_PAYMENT_METHOD_ALREADY_EXISTS)
    
    def get_response_for_add_payment_method_to_order(self, payment_id:int):
        
        return {
            "payment_id": payment_id
        }
    
    def get_response_for_create_refund_request(self, refund_id:int):
        
        return {
            "refund_id": refund_id
        }
    
    def raise_exception_for_refund_request_does_not_exist(self):
        raise NotFound(*exception_messages.REFUND_REQUEST_DOES_NOT_EXIST)
    
    def get_response_for_update_refund_status_after_refunded(self):

        return {
            "success": "refund status updated successfully"
        }