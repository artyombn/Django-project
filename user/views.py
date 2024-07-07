from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View

from idea.models import Idea
from .models import User, Follow
from .forms import RegisterForm, UserProfileForm
from .group_permission import GroupRequiredMixin


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

    def checkfollow(self):
        ruser = self.request.user
        user = self.object
        if (user.follower.filter(follower=user, following=ruser).exists()):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = UserProfileForm(instance=self.object)
        context['ideas'] = Idea.objects.filter(author=self.object)
        context['check'] = self.checkfollow()
        return context



    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})


class UserListView(GroupRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'

    group_name = ["User"]

    def test_func(self):
        return self.staff_permission()

    def staff_permission(self):
        return self.request.user.is_staff


class Followers(ListView):
    model = Follow
    context_object_name = 'followers'

class FollowUser(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ruser = request.user
        if Follow.objects.filter(follower=user, following=ruser).exists():
            follow = Follow.objects.get(follower=user, following=ruser)
            follow.delete()
            return redirect(reverse('users:profile', kwargs={'pk': pk}))
        else:
            follow_create = Follow()
            follow_create.follower = user
            follow_create.following = ruser
            follow_create.save()
            return redirect(reverse('users:profile', kwargs={'pk': pk}))
