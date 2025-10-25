from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'date', 'category', 'amount', 'description', 
            'payment_mode', 'merchant_name', 'location', 
            'notes', 'created_by'
        ]
