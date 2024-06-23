from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
from .forms import RegisterForm



class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('users:users_list')


class AuthView(LoginView):
    template_name = 'user/login.html'


class ExitView(LogoutView):
    pass



def users_list_view(request):

    users = User.objects.all()
    return render(request, "user/list.html", {"users": users})
