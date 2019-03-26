from django.db import models
from datetime import date

class Expense(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(blank=False, null=False, default=date.today)
    class Meta:
        db_table = "expenses"