class PaymentMethodAlreadyExistsException(Exception):
    pass

class PaymentMethodDoesNotExistException(Exception):
    def __init__(self, paymentmethod_id:int):
        self.paymentmethod_id = paymentmethod_id

    def __str__(self):
        return f"{self.paymentmethod_id} does not exist"

class RefundDoesNotExistException(Exception):
    def __init__(self, refund_id:int):
        self.refund_id = refund_id

    def __str__(self):
        return f"{self.refund_id} does not exist"