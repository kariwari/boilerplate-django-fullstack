from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags


def send_email_task(subject, message, to_email):
    send_mail(
        subject=subject,
        message=strip_tags(message),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        html_message=message,
        fail_silently=False,
    )
