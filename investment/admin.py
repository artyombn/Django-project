from django.contrib import admin
from investment.models import Investor, InvestorPayment

admin.site.register(Investor)
admin.site.register(InvestorPayment)