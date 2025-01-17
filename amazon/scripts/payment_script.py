from amazon.models import PaymentMethod
from amazon.models import Payment

def create_payment_method():

    payment_method_data = {
    "payment_type": "Credit Card",
    "card_type": "Visa",
    "card_number": "4111111111111111",
    "card_holder_name": "John Doe",
    "expiry_date": "12/25",
    "cvv": "123"
    }
    
    PaymentMethod.objects.create(payment_type=payment_method_data['payment_type'], card_type=\
                                                  payment_method_data['card_type'], card_number=payment_method_data['card_number'], \
                                                    card_holder_name=payment_method_data['card_holder_name'], \
                                                        expiry_date=payment_method_data['expiry_date'], cvv=payment_method_data['cvv'])
    
def create_payment():

    payment_data = {
    "order_id": 1,
    "payment_method_id": 1,
    "amount": 1000.00,
    "payment_status": "Success",
    "transaction_id": "1234567890"
    }
    
    Payment.objects.create(order_id=payment_data['order_id'], payment_method_id=payment_data['payment_method_id'], \
                                      amount=payment_data['amount'], payment_status=payment_data['payment_status'], \
                                        transaction_id=payment_data['transaction_id'])
