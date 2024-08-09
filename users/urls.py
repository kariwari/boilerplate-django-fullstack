from django.urls import path, reverse_lazy

# from django.contrib.auth.views import (
#     PasswordChangeView,
#     PasswordResetView,
#     PasswordResetDoneView,
#     PasswordResetConfirmView,
#     PasswordResetCompleteView,
# )
from django.views.generic import TemplateView


# from .views import (
#     EmailVerificationView,
#     UserRegisterView,
#     UserLoginView,
#     UserLogoutView,
#     UserProfileView,
#     ListAddressView,
#     UpdateOrCreateAddressView,
#     DeleteAddressView,
# )
# from .forms import CustomPasswordResetForm, CustomPasswordChangeForm

app_name = "users"
urlpatterns = [
    path(
        "login/",
        TemplateView.as_view(template_name="users/auth/login.html"),
        name="login",
    ),
    path(
        "register/",
        TemplateView.as_view(template_name="users/auth/register.html"),
        name="register",
    ),
    path(
        "forgot-password/",
        TemplateView.as_view(template_name="users/auth/forgot-password.html"),
        name="forgot-password",
    ),
    path(
        "set-new-password/",
        TemplateView.as_view(template_name="users/auth/set-new-password.html"),
        name="set-new-password",
    ),
    path(
        "",
        TemplateView.as_view(template_name="users/profile.html"),
        name="profile",
    ),
    path(
        "change-password/",
        TemplateView.as_view(template_name="users/change-password.html"),
        name="change-password",
    ),
]
