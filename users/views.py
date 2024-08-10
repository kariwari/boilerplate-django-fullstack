from django.contrib import messages, auth
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile

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


class UserLoginView(View):
    template_name = "users/auth/login.html"
    form_class = UserLoginForm

    def get(self, request):
        next_url = request.GET.get("next")
        if next_url:
            messages.info(request, "Please login to continue the process..")

        if request.user.is_authenticated:
            return redirect("users:profile")

        form = self.form_class()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        next_url = request.POST.get("next")

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(email=email, password=password)

            if user is not None:
                # email_address = EmailAddress.objects.get(user=user)
                # if email_address.is_verified:
                auth.login(request, user)
                if next_url:
                    return redirect(next_url)
                if user.is_superuser:
                    return redirect("panels:dashboard")
                return redirect("users:profile")
            # else:
            #     messages.error(
            #         request, "Silakan verifikasi email Anda sebelum login."
            #     )
            else:
                messages.error(request, "Login failed. Please check your credentials.")

        return render(request, self.template_name, {"form": form, "next": next_url})


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(
                request, "You have successfully logged out from your account!"
            )
        return super().dispatch(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users/user_profile.html"

    def get_object(self):
        user_id = self.request.user.profile.id
        return get_object_or_404(Profile, pk=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Manage Profile"
        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        if form.has_changed():
            print("PING")
            response = super().form_valid(form)
            messages.success(self.request, "Your biodata has been successfully updated")
            return response
        else:
            print("PONG")
            messages.info(self.request, "There are no changes to your biodata")
            return redirect(self.get_success_url())
