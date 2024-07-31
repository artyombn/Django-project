from celery import shared_task

# from celery.exceptions import SoftTimeLimitExceeded
# from yookassa import Payment
from .models import InvestorPayment
import time

@shared_task(name='check_payment_status')
def check_payment_status():
    print("Starting task")
    a = InvestorPayment.objects.all()
    print(f'a = {a}')
    time.sleep(10)
    print("Test task finished")
    return a


    # pending_payments = InvestorPayment.objects.filter(status='pending')
    # if pending_payments:

            # for payment in pending_payments:
            #     yookassa_payment = Payment.find_one(payment.payment_id)
            #     if yookassa_payment.status == 'succeeded':
            #         payment.status = 'succeeded'
            #     elif yookassa_payment.status == 'failed':
            #         payment.status = 'failed'
            #     elif yookassa_payment.status == 'waiting_for_capture':
            #         payment.status = 'waiting_for_capture'
            #     else:
            #         payment.status = 'pending'
            #     payment.save()
            #     print(f"Task completed successfully {payment}")
        # else:
        #     print(f"No pending payments")
