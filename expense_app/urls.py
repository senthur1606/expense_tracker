from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('expense/add/', views.expense_create, name='expense_create'),
    path('expense/update/<int:expense_id>/', views.expense_update, name='expense_update'),
    path('expense/delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),
    path('expense/summary/', views.expense_summary, name='expense_summary'),
]
