from django.urls import path, reverse_lazy

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views.generic import TemplateView, RedirectView


from .views import (
    EmailVerificationView,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
)

from .forms import CustomPasswordChangeForm, CustomPasswordResetForm

app_name = "users"
urlpatterns = [
    # Profile
    path("", RedirectView.as_view(url=reverse_lazy("users:profile"))),
    path(
        "profile/",
        UserProfileView.as_view(),
        name="profile",
    ),
    # Authentication
    path(
        "auth/register/",
        UserRegisterView.as_view(),
        name="register",
    ),
    path(
        "auth/verify-email/<uuid:token>/",
        EmailVerificationView.as_view(),
        name="verify_email",
    ),
    path(
        "auth/login/",
        UserLoginView.as_view(),
        name="login",
    ),
    path("auth/logout/", UserLogoutView.as_view(), name="logout"),
    # Change Password
    path(
        "profile/change-password/",
        PasswordChangeView.as_view(
            template_name="users/auth/password_change_form.html",
            form_class=CustomPasswordChangeForm,
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "profile/change-password/done/",
        TemplateView.as_view(
            template_name="users/auth/password_change_done.html",
        ),
        name="password_change_done",
    ),
    # Password Reset
    path(
        "auth/password-reset/",
        PasswordResetView.as_view(
            template_name="users/auth/password_reset_form.html",
            form_class=CustomPasswordResetForm,
            email_template_name="users/email/password_reset_email.html",
            html_email_template_name="users/email/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "auth/password-reset-sent/",
        PasswordResetDoneView.as_view(
            template_name="users/auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "auth/password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/auth/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "auth/password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # path(
    #     "forgot-password/",
    #     TemplateView.as_view(template_name="users/auth/forgot-password.html"),
    #     name="forgot-password",
    # ),
    # path(
    #     "set-new-password/",
    #     TemplateView.as_view(template_name="users/auth/set-new-password.html"),
    #     name="set-new-password",
    # ),
]
