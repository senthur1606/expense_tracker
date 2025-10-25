from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.expense_create, name='expense_create'),
    path('update/<int:id>/', views.expense_update, name='expense_update'),
    path('delete/<int:id>/', views.expense_delete, name='expense_delete'),
    path('summary/', views.expense_summary, name='expense_summary'),
]
