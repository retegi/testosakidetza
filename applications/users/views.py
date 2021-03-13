from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    FormView
)
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    ListView
)
from django.urls import reverse_lazy, reverse
from .forms import (
    LoginForm,
    UserRegisterForm
)

from .models import User


# Create your views here.
class HomePageView(TemplateView):
    template_name = "users/index.html"

"""class LoginView(TemplateView):
    template_name = "users/login.html"""

class UserRegistrationView(FormView):
    template_name = "users/user_registration.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:home')




class UserLoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)

class UserLogoutView(FormView):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'home_app:home'
            )
        )
