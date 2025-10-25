from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.db.models import Sum

# List all expenses
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})


# Add expense (CREATE)
def expense_create(request):
    if request.method == 'POST':
        Expense.objects.create(
            date=request.POST.get('date'),
            category=request.POST.get('category'),
            amount=request.POST.get('amount'),
            description=request.POST.get('description'),
            payment_mode=request.POST.get('payment_mode'),
            merchant_name=request.POST.get('merchant_name'),
            location=request.POST.get('location'),
            notes=request.POST.get('notes'),
            created_by=request.POST.get('created_by')
        )
        return redirect('expense_list')  # ✅ redirect after save

    return render(request, 'expense_form.html')  # ✅ render form page


# Update expense
def expense_update(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.date = request.POST.get('date')
        expense.category = request.POST.get('category')
        expense.amount = request.POST.get('amount')
        expense.description = request.POST.get('description')
        expense.payment_mode = request.POST.get('payment_mode')
        expense.merchant_name = request.POST.get('merchant_name')
        expense.location = request.POST.get('location')
        expense.notes = request.POST.get('notes')
        expense.created_by = request.POST.get('created_by')
        expense.save()
        return redirect('expense_list')
    return render(request, 'expense_form.html', {'expense': expense})


# Delete expense
def expense_delete(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense_list')


# Summary by category
def expense_summary(request):
    summary = Expense.objects.values('category').annotate(total=Sum('amount'))
    return render(request, 'expense_summary.html', {'summary': summary})
