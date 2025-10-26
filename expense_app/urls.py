from django.urls import path
from expense_app import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('expense/add/', views.expense_create, name='expense_create'),
    path('expense/<int:pk>/update/', views.expense_update, name='expense_update'),
    path('expense/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    path('expense/summary/', views.expense_summary, name='expense_summary'),
    path('expense/<int:pk>/confirm-delete/', views.expense_confirm_delete, name='expense_confirm_delete'),
    path('expense/export/pdf/', views.export_expenses_pdf, name='export_expenses_pdf'),
    path('expense/export/excel/', views.export_expenses_excel, name='export_expenses_excel'),
]
