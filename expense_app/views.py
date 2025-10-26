from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from expense_app.models import Expense
from django.db.models import Sum
from django.template.loader import get_template
from xhtml2pdf import pisa
import openpyxl
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
        return redirect('expense_list')  #  redirect after save

    return render(request, 'expense_form.html')  #  render form page


# Update expense
def expense_update(request, pk):
    expense = get_object_or_404(Expense, id=pk)
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
    total_amount = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    category_totals = (
        Expense.objects
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('category')
    )

    # Make it an empty list if no records found
    if not category_totals.exists():
        category_totals = []

    context = {
        'total_amount': total_amount,
        'category_totals': category_totals
    }
    return render(request, 'expense_summary.html', context)

def expense_confirm_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'expense_confirm_delete.html', {'expense': expense})


#-----------Export expenses as PDF--------------


def export_expenses_pdf(request):
    category_totals = (
        Expense.objects
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('category')
    )
    total_amount = Expense.objects.aggregate(total=Sum('amount'))['total'] or 0
    template_path = 'expense_summary_pdf.html'
    context = {'category_totals': category_totals, 'total_amount': total_amount}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="expense_summary.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF <pre>' + html + '</pre>')
    return response

# -------------------- Export Excel --------------------
def export_expenses_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Expense Summary"
    ws.append(['Category', 'Total Amount'])

    category_totals = (
        Expense.objects
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('category')
    )

    for item in category_totals:
        ws.append([item['category'], float(item['total'])])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=expense_summary.xlsx'
    wb.save(response)
    return response