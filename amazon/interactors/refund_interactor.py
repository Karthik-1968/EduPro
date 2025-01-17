from amazon.interactors.storage_interfaces.user_storage_interface import UserStorageInterface
from amazon.interactors.presenter_interfaces.user_presenter_interface import UserPresenterInterface
from amazon.interactors.storage_interfaces.order_storage_interface import OrderStorageInterface
from amazon.interactors.presenter_interfaces.order_presenter_interface import OrderPresenterInterface
from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.presenter_interfaces.payment_presenter_interface import PaymentPresenterInterface
from amazon.exceptions import payment_custom_exceptions, user_custom_exceptions, order_custom_exceptions
from amazon.interactors.storage_interfaces.dtos import RefundDTO

class RefundInteractor:

    def __init__(self, user_storage: UserStorageInterface, order_storage: OrderStorageInterface, \
                 payment_storage: PaymentStorageInterface):
        
        self.user_storage = user_storage
        self.order_storage = order_storage
        self.payment_storage = payment_storage


    def create_refund_request_wrapper(self, refund_dto: RefundDTO, user_presenter: UserPresenterInterface, \
                                      order_presenter: OrderPresenterInterface, payment_presenter: PaymentPresenterInterface):

        try:
            refund_id = self.create_refund_request(refund_dto=refund_dto)
        except user_custom_exceptions.UserDoesNotExistException:
            user_presenter.raise_exception_for_user_does_not_exist()
        except order_custom_exceptions.OrderDoesNotExistException:
            order_presenter.raise_exception_for_order_does_not_exist()
        else:
            return payment_presenter.get_response_for_create_refund_request(refund_id=refund_id)

    def create_refund_request(self, refund_dto: RefundDTO):

        """ELP
            -check if user exists
            -check if order exists
            -create refund request
        """

        self.user_storage.check_if_user_exists(user_id=refund_dto.user_id)

        self.order_storage.check_if_order_exists(order_id=refund_dto.order_id)

        return self.payment_storage.create_refund_request(refund_dto=refund_dto)
    

    def update_refund_status_after_refunded_wrapper(self, refund_id: int, payment_presenter: PaymentPresenterInterface):
        
        try:
            self.update_refund_status_after_refunded(refund_id=refund_id)
        except payment_custom_exceptions.RefundDoesNotExistException:
            payment_presenter.raise_exception_for_refund_does_not_exist()
        else:
            return payment_presenter.get_response_for_update_refund_status_after_refunded()
    
    def update_refund_status_after_refunded(self, refund_id: int):

        """ELP
            -check if refund exists
            -update refund status after refunded
        """

        self.payment_storage.check_if_refund_exists(refund_id=refund_id)

        return self.payment_storage.update_refund_status_after_refunded(refund_id=refund_id)

