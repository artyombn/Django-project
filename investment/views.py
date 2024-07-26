from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView

from investment.models import Investor


class InvestorsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Investor
    template_name = 'investments/investors.html'

    def test_func(self):
        return self.is_user_in_group()

    def is_user_in_group(self):
        return self.request.user.is_staff or self.request.user.groups.filter(name="Investor").exists()
