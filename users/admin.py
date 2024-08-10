from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin class to manage custom users in Django admin panel.
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_per_page = 15
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class to manage user profiles in Django admin panel.
    """

    list_display = (
        "display_full_name",
        "display_email",
        "photo",
        "created_at",
        "updated_at",
    )
    list_per_page = 15
    search_fields = ("user__email", "first_name", "last_name")

    def display_full_name(self, obj):
        """
        Display the user's full name. If first or last name is blank, display the user ID.
        """
        return obj.get_full_name() if obj.first_name and obj.last_name else obj.pk

    display_full_name.short_description = "Nama Lengkap"

    def display_email(self, obj):
        """
        Show user email.
        """
        return obj.user.email

    display_email.short_description = "Email"
