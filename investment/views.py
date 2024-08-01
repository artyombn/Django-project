from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views import View

from investment.models import Investor, InvestorPayment
from investment.payments import create_payment, fetch_all_payments

from yookassa import Payment


class InvestorsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Investor
    template_name = 'investments/investors.html'

    def test_func(self):
        return self.is_user_in_group()

    def is_user_in_group(self):
        return self.request.user.is_staff or self.request.user.groups.filter(name="Investor").exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        investor_payments = InvestorPayment.objects.all()
        context['all_payments'] = fetch_all_payments()
        context['all_investor_payments'] = investor_payments

        # pending_payments = InvestorPayment.objects.filter(status='pending')
        # if pending_payments:
        #     for payment in pending_payments:
        #         yookassa_payment = Payment.find_one(payment.payment_id)
        #         print(f"yookassa_payment = {yookassa_payment.status}")
        #         print(f"payment.status BEFORE = {payment.status}")
        #         payment.status = yookassa_payment.status
        #         payment.save()
        #         print(f"payment.status after = {payment.status}")
        # else:
        #     print(f"No pendings")
        return context

class CreatePaymentView(View):
    def get(self, request):
        return render(request, 'investments/payment.html')

    def post(self, request):
        user = self.request.user
        amount = float(request.POST.get('amount'))
        full_url = request.build_absolute_uri('/investments/payment-check/')
        confirmation_url, payment_id = create_payment(amount, full_url, user)

        payment_detail = Payment.find_one(payment_id)
        payment_detail_dict = {
            'id': payment_detail.id,
            'status': payment_detail.status,
        }
        request.session['payment_detail'] = payment_detail_dict

        return redirect(confirmation_url)


class PaymentCheckView(View):
    def get(self, request):
        payment_detail_dict = request.session.get('payment_detail')

        # if 'payment_detail' in request.session:
        #     del request.session['payment_detail']

        context = {'payment_detail': payment_detail_dict}

        return render(request, 'investments/payment_check.html', context)