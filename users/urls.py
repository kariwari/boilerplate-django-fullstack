from django.urls import path, reverse_lazy

# from django.contrib.auth.views import (
#     PasswordChangeView,
#     PasswordResetView,
#     PasswordResetDoneView,
#     PasswordResetConfirmView,
#     PasswordResetCompleteView,
# )
from django.views.generic import TemplateView


from .views import (
    #     EmailVerificationView,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    #     ListAddressView,
    #     UpdateOrCreateAddressView,
    #     DeleteAddressView,
)

# from .forms import CustomPasswordResetForm, CustomPasswordChangeForm

app_name = "users"
urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register",
    ),
    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),
    path("logout/", UserLogoutView.as_view(), name="logout"),
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
        UserProfileView.as_view(),
        name="profile",
    ),
    path(
        "change-password/",
        TemplateView.as_view(template_name="users/change-password.html"),
        name="change-password",
    ),
]
