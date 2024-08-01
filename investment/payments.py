from yookassa import Payment
import uuid
from .yookassa_config import Configuration

from decimal import Decimal
from pprint import pprint


from investment.models import InvestorPayment

def create_payment(amount, return_url, user):
    idempotence_key = str(uuid.uuid4()) # generate idempotency_key
    payment = Payment.create({
        "amount": {
            "value": f"{amount:.2f}",
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": return_url
        },
        "description": "Test Order#1"
    }, idempotence_key)

    investor_payment = InvestorPayment.objects.create(
        user=user,
        payment_id = payment.id,
        amount=Decimal(payment.amount['value']),
        created_at = payment.created_at,
        description = payment.description,
        payment_method =  payment.payment_method.type,
        status = payment.status,
    )
    payment_id = payment.id

    return payment.confirmation.confirmation_url, payment_id

def fetch_all_payments():
    yookassa_all_payments = Payment.list()
    payments_list = dict(yookassa_all_payments).values()

    res = list()
    for value in payments_list:
        for dd in value:
            if isinstance(dd, dict):
                res.append(dd)
    return res