from amazon.interactors.storage_interfaces.payment_storage_interface import PaymentStorageInterface
from amazon.interactors.storage_interfaces.dtos import CardPaymentMethodDTO, NetBankingPaymentMethodDTO, OrderPaymentDTO, RefundDTO
from amazon.models import PaymentMethod, Payment, Order, Refund
from amazon.exceptions import payment_custom_exceptions

class PaymentStorageImplementation(PaymentStorageInterface):

    def create_card_payment_method(self, cardpaymentmethod_dto:CardPaymentMethodDTO)->int:
        
        paymentmethod = PaymentMethod.objects.create(
            payment_type = cardpaymentmethod_dto.payment_type,
            card_name = cardpaymentmethod_dto.card_name,
            card_number = cardpaymentmethod_dto.card_number,
            card_holder_name = cardpaymentmethod_dto.card_holder_name,
            cvv = cardpaymentmethod_dto.cvv,
            expiry_date = cardpaymentmethod_dto.expiry_date,
            card_type = cardpaymentmethod_dto.card_type
        )

        return paymentmethod.id
    

    def create_net_banking_payment_method(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO)->int:
        
        paymentmethod = PaymentMethod.objects.create(
            payment_type=netbankingpaymentmethod_dto.payment_type,
            bank_name=netbankingpaymentmethod_dto.bank_name,
            username=netbankingpaymentmethod_dto.username,
            password=netbankingpaymentmethod_dto.password
        )

        return paymentmethod.id
    

    def create_upi_payment_method(self, payment_type:str, upi_id:str)->int:

        paymentmethod = PaymentMethod.objects.create(
            payment_type=payment_type,
            upi_id=upi_id
        )

        return paymentmethod.id
    
    def create_cash_on_delivery_payment_method(self, payment_type:str)->int:

        paymentmethod = PaymentMethod.objects.create(
            payment_type=payment_type
        )

        return paymentmethod.id
    
    def check_if_card_payment_method_already_exists(self, cardpaymentmethod_dto:CardPaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=cardpaymentmethod_dto.payment_type, card_name=cardpaymentmethod_dto.card_name,\
                                        card_number=cardpaymentmethod_dto.card_number, \
                                         card_holder_name=cardpaymentmethod_dto.card_holder_name, \
                                             cvv=cardpaymentmethod_dto.cvv, expiry_date=cardpaymentmethod_dto.expiry_date, \
                                                 card_type=cardpaymentmethod_dto.card_type).exists():
            raise payment_custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_net_banking_payment_method_already_exists(self, netbankingpaymentmethod_dto:NetBankingPaymentMethodDTO):

        if PaymentMethod.objects.filter(payment_type=netbankingpaymentmethod_dto.payment_type, bank_name=netbankingpaymentmethod_dto.bank_name, \
                                        username=netbankingpaymentmethod_dto.username, password=netbankingpaymentmethod_dto.password).exists():
            raise payment_custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_upi_payment_method_already_exists(self, payment_type:str, upi_id:str):

        if PaymentMethod.objects.filter(payment_type=payment_type, upi_id=upi_id).exists():
            raise payment_custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_cash_on_delivery_payment_method_already_exists(self, payment_type:str):

        if PaymentMethod.objects.filter(payment_type=payment_type).exists():
            raise payment_custom_exceptions.PaymentMethodAlreadyExistsException
        
    def check_if_payment_method_exists(self, paymentmethod_id:int):

        paymentmethod = PaymentMethod.objects.filter(id=paymentmethod_id).exists()
        paymentmethod_not_exists = not paymentmethod

        if paymentmethod_not_exists:
            raise payment_custom_exceptions.PaymentMethodDoesNotExistException(paymentmethod_id=paymentmethod_id)
        
    def add_payment_method_to_order(self, orderpayment_dto:OrderPaymentDTO)->int:
        
        payment = Payment.objects.create(
            order_id=orderpayment_dto.order_id,
            payment_method_id=orderpayment_dto.payment_method_id,
            amount=orderpayment_dto.amount,
            payment_status=orderpayment_dto.payment_status,
            transaction_id=orderpayment_dto.transaction_id
        )

        return payment.id
    
    def create_refund_request(self, refund_dto:RefundDTO)->int:

        refund = Refund.objects.create(
            user_id=refund_dto.user_id,
            order_id=refund_dto.order_id,
            amount=refund_dto.amount,
            refund_status=refund_dto.refund_status,
            payment_date=refund_dto.payment_date,
            reason=refund_dto.reason
        )

        return refund.id
    
    def check_if_refund_exists(self, refund_id:int):
        
        refund = Refund.objects.filter(id=refund_id).exists()
        refund_not_exists = not refund

        if refund_not_exists:
            raise payment_custom_exceptions.RefundDoesNotExistException(refund_id=refund_id)
        
    
    def update_refund_status_after_refunded(self, refund_id:int):
        
        refund = Refund.objects.get(id=refund_id)
        refund.refund_status = "Refunded"
        refund.save()

        refund.order.order_status = "Refunded"
        refund.order.save()