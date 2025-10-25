from django.core.management.base import BaseCommand
from expense_app.models import Expense
from datetime import datetime

class Command(BaseCommand):
    help = "Console-based CRUD for Expenses"

    def handle(self, *args, **options):
        while True:
            print("\n1. Add Expense\n2. List Expenses\n3. Delete Expense\n4. Exit")
            choice = input("Choose: ")
            if choice == '1':
                category = input("Category: ")
                amount = input("Amount: ")
                Expense.objects.create(
                    category=category,
                    amount=amount,
                    date=datetime.today(),
                    payment_mode='Cash',
                    created_by_id=1
                )
                print("Expense Added.")
            elif choice == '2':
                for e in Expense.objects.all():
                    print(e)
            elif choice == '3':
                eid = input("Enter Expense ID to delete: ")
                e = Expense.objects.filter(expense_id=eid).first()
                if e:
                    e.delete()
                    print("Deleted")
            elif choice == '4':
                break
