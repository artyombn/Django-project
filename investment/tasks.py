from celery import shared_task

from celery.exceptions import SoftTimeLimitExceeded
from yookassa import Payment
from .models import InvestorPayment

@shared_task(name='check_payment_status')
def check_payment_status():
    pending_payments = InvestorPayment.objects.exclude(status__in=['succeeded', 'failed'])

    if pending_payments:
        for payment in pending_payments:
            yookassa_payment = Payment.find_one(payment.payment_id)
            if yookassa_payment.status == 'succeeded':
                payment.status = 'succeeded'
                payment.paid = True
            elif yookassa_payment.status == 'failed':
                payment.status = 'failed'
                payment.paid = False
            elif yookassa_payment.status == 'waiting_for_capture':
                payment.status = 'waiting_for_capture'
                payment.paid = False
            else:
                payment.status = 'pending'
                payment.paid = False
            payment.save()
            print(f"Task completed successfully {payment}")
    else:
        print(f"No pending payments")


