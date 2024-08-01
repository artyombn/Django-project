from django.urls import path
from investment import views

app_name = 'investment'

urlpatterns = [
    path('', views.InvestorsView.as_view(), name='list'),
    path('payment/', views.CreatePaymentView.as_view(), name='payment'),
    path('payment-check/', views.PaymentCheckView.as_view(), name='payment_check'),
]