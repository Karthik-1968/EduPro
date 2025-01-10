from amazon.interactors.storage_interfaces.storage_interface import StorageInterface
from amazon.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from amazon.exceptions import custom_exceptions
from amazon.interactors.storage_interfaces.storage_interface import RefundDTO

class RefundInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter


    def create_refund_request_wrapper(self, user_id:str, order_id:int, amount:float, refund_status:str, payment_date:int, \
                                      reason:str):
        refund_dto = RefundDTO(user_id=user_id, order_id=order_id, amount=amount, refund_status=refund_status, \
                               payment_date=payment_date, reason=reason)
        try:
            refund_id = self.create_refund_request(refund_dto=refund_dto)
        except custom_exceptions.UserDoesNotExist:
            self.presenter.raise_exception_for_user_does_not_exist()
        except custom_exceptions.OrderDoesNotExist:
            self.presenter.raise_exception_for_order_does_not_exist()
        else:
            return self.presenter.get_response_for_create_refund_request(refund_id=refund_id)

    def create_refund_request(self, refund_dto: RefundDTO):

        """ELP
            -check if user exists
            -check if order exists
            -create refund request
        """

        self.storage.check_if_user_exists(user_id=refund_dto.user_id)

        self.storage.check_if_order_exists(order_id=refund_dto.order_id)

        return self.storage.create_refund_request(refund_dto=refund_dto)
    

    def update_refund_status_after_refunded_wrapper(self, refund_id: int):
        try:
            self.update_refund_status_after_refunded(refund_id=refund_id)
        except custom_exceptions.RefundDoesNotExistException:
            self.presenter.raise_exception_for_refund_does_not_exist()
        else:
            return self.presenter.get_response_for_update_refund_status_after_refunded()
    
    def update_refund_status_after_refunded(self, refund_id: int):

        """ELP
            -check if refund exists
            -update refund status after refunded
        """

        self.storage.check_if_refund_exists(refund_id=refund_id)

        return self.storage.update_refund_status_after_refunded(refund_id=refund_id)

