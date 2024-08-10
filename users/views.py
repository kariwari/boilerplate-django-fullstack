from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from .forms import UserRegisterForm

UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    template_name = "users/auth/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("users:profile")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Register Account"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        messages.success(
            self.request,
            f"Please check your email <strong>{email}</strong> to verify your account.",
        )
        return response
