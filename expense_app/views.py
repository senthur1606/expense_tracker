from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm

# List all expenses
def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expense_list.html', {'expenses': expenses})

# Create new expense

def expense_create(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        payment_mode = request.POST.get('payment_mode')
        merchant_name = request.POST.get('merchant_name')
        location = request.POST.get('location')
        notes = request.POST.get('notes')
        created_by = request.POST.get('created_by')

        Expense.objects.create(
            date=date,
            category=category,
            amount=amount,
            description=description,
            payment_mode=payment_mode,
            merchant_name=merchant_name,
            location=location,
            notes=notes,
            created_by=created_by
        )
        return redirect('expense_list')  # After save, go back to list page

    return render(request, 'expense_form.html')
# Update existing expense
def expense_update(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_form.html', {'form': form})

# Delete expense
def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_confirm_delete.html', {'expense': expense})

# Expense summary
def expense_summary(request):
    summary = Expense.objects.values('category').annotate(total=Sum('amount'))
    return render(request, 'expense_summary.html', {'summary': summary})
