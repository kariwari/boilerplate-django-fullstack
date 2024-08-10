from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from .models import Profile

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

        for name, field in self.fields.items():
            field.help_text = None

            if name == "email":
                field.widget.attrs.update({"placeholder": "Enter email"})

            if name == "password1":
                field.widget.attrs.update({"placeholder": "Enter password"})

            if name == "password2":
                field.widget.attrs.update({"placeholder": "Enter password again"})

        for field in self.fields.values():
            field.error_messages = {
                "required": "{fieldname} must be filled".format(fieldname=field.label),
                "unique": "This email address is already registered",
            }


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your Email",
            }
        ),
        error_messages={"required": "Email must be filled"},
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your Password",
            }
        ),
        error_messages={"required": "Password must be filled"},
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"

        for _, field in self.fields.items():
            field.help_text = None

            field.required = True

            field.widget.attrs.update(
                {
                    "placeholder": "Enter your {fieldname}".format(
                        fieldname=field.label
                    ),
                }
            )

        for field in self.fields.values():
            field.error_messages = {
                "required": "{fieldname} must be filled".format(fieldname=field.label),
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
