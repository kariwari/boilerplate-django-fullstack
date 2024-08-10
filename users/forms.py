from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].label = "Email"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"

        self.fields["email"].required = True

        self.error_messages["password_mismatch"] = (
            "Password does not match. Please try again."
        )

        for field in self.fields.values():
            field.error_messages = {
                "required": "{fieldname} must be filled".format(fieldname=field.label),
                "unique": "This email address is already registered",
            }


# Form for Django Admin Panel
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ("email",)
