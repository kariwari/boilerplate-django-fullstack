from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailAddress, Profile


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_and_send_verification(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user, email=user.email)

        email_address = EmailAddress.objects.create(user=user, email=user.email)
        email_address.send_verification_email()
