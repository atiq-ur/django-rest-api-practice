from django.core.mail import send_mail
from decouple import config

class Utils:
    @staticmethod
    def send_mail(data):
        send_mail(
            subject=data['subject'],
            message=data['body'],
            from_email=config('MAIL_FROM_ADDRESS'),
            recipient_list=[data['email']],
            fail_silently=False,  # Set to True for production to avoid unhandled exceptions
        )
