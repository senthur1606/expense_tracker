from django.db import models

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    payment_mode = models.CharField(max_length=50)
    merchant_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
