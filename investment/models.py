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
    status = models.CharField(max_length=15, choices=choices2)
    note = models.TextField(blank=True, null=True)

    # equity_percentage

    def __str__(self):
        return (f'{self.user} - {self.idea} - invested {self.amount_invested}')