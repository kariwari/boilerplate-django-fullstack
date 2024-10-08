from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.utils import timezone
import uuid
import os
import django_rq

from django_project.tasks import send_email_task
from .utils import CustomUserManager, photo_path


class CustomUser(AbstractUser):
    """
    A custom user model that uses email as the primary identifier.
    """

    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_("Email Address"), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class EmailAddress(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="email_address", on_delete=models.CASCADE
    )
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(
        default=uuid.uuid4, blank=True, null=True, unique=True
    )
    sent_at = models.DateTimeField(null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

    def send_verification_email(self):
        current_site = Site.objects.get_current()
        verification_link = reverse(
            "users:verify_email", args=[self.verification_token]
        )
        verification_url = f"http://{current_site.domain}{verification_link}"

        subject = "Verifikasi Email Anda"
        message = render_to_string(
            "users/email/email_confirmation_message.html",
            {
                "verification_url": verification_url,
                "user": self.user,
            },
        )

        django_rq.enqueue(
            send_email_task,
            subject=subject,
            message=message,
            to_email=self.email,
        )

        self.sent_at = timezone.now()
        self.save()


class Profile(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    user = models.OneToOneField(
        CustomUser,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    photo = models.ImageField(
        null=True, blank=True, upload_to=photo_path, default="default.png"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def get_full_name(self):
        """
        Returns the user's full name, which is a combination of the first and last name.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        """
        A string representation of the profile, using full name if available, or email if not.
        """
        full_name = self.get_full_name()
        return full_name if full_name else self.user.email

    def save(self, *args, **kwargs):
        """
        Ensures old photos are removed from the filesystem when profile photos are updated.
        """
        if self.pk:
            try:
                old_photo = Profile.objects.get(pk=self.pk).photo
            except Profile.DoesNotExist:
                pass
            else:
                if (
                    old_photo
                    and old_photo.name != self.photo.name
                    and old_photo.name != "default.png"
                ):
                    old_photo_path = os.path.join(settings.MEDIA_ROOT, old_photo.name)
                    if os.path.isfile(old_photo_path):
                        os.remove(old_photo_path)
                elif not self.photo:
                    self.photo.name = "default.png"  # TODO: If unchecked from admin panels, then save it as default photo.

        super(Profile, self).save(*args, **kwargs)
