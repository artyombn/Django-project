from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

from idea.models import Idea
from .models import User
from .forms import RegisterForm, UserProfileForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('users:users_list')


class AuthView(LoginView):
    template_name = 'user/login.html'


class ExitView(LogoutView):
    pass

class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user/profile.html'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = UserProfileForm(instance=self.object)
        context['ideas'] = Idea.objects.filter(author=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})

def users_list_view(request):

    users = User.objects.prefetch_related('groups').all()
    return render(request, "user/list.html", {"users": users})
