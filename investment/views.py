from django.shortcuts import render
from django.views.generic import ListView
from investment.models import Investor


class InvestorsView(ListView):
    model = Investor
    template_name = 'investments/investors.html'

