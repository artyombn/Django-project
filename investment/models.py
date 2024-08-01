from django.db import models

class Investor(models.Model):
    choices1 = [
        ('shares', 'Shares'),
        ('debt', 'Debt'),
        ('other', 'Other')
    ]

    choices2 = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]


    idea = models.ForeignKey('idea.Idea', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    investment_type = models.CharField(max_length=50, choices=choices1)
    status = models.CharField(max_length=50, choices=choices2)
    note = models.TextField(blank=True, null=True)
    payment = models.ForeignKey('investment.InvestorPayment', on_delete=models.CASCADE, null=True, blank=True)

    # equity_percentage

    def __str__(self):
        return (f'{self.user} - {self.idea} - invested {self.amount_invested}')


class InvestorPayment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    payment_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField()
    description = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return (f"User: {self.user}, "
                f"payment id <{self.payment_id}>, "
                f"amount = {self.amount}, "
                f"created = {self.created_at}, "
                f"description = {self.description}, "
                f"paid = {self.paid} ,"
                f"payment_method = {self.payment_method} ,"
                f"status = {self.status}")