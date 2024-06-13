import time
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_admin_message(message):
    time.sleep(30)
    send_mail(
        "Admin message",
        message,
        "admin@brainwave.com",
        ["admin@brainwave.com", "help@brainwave.com"],
        fail_silently=False,
    )
    return 15