from datetime import datetime, timedelta
from django.core.mail import send_mail
from config import settings
from .celery import app

# from celery.utils.log import get_logger
# logger = get_logger(__name__)

@app.task
def send_email_task(recipients, subject, message):
    send_mail(recipient_list=[recipients, ],
              subject=subject,
              message=message,
              from_email=settings.DEFAULT_FROM_EMAIL,
              fail_silently=False
              )


def append_task(email, text, delay, duetime):
    duetime += timedelta(minutes=delay)
    print('===ETA===>', duetime)
    exp = datetime.now() + timedelta(seconds=5)
    send_email_task.apply_async((email, 'Subject message test', text), expires=exp)
    #send_email_task.apply_async((email, 'Subject message test', text), countdown=4)

