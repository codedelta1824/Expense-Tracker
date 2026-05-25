from Storage import StorageManager
from datetime import date

class ExpenseEngine:
    def __init__(self):
        self.expenses = StorageManager.load_data()

    def add_expense(self, amount_str, category, description):
        """Validates input, appends to the list, and saves to storage."""
        if not amount_str or not category or not description:
            return False, "All fields are required."
            
        try:
            amount_float = float(amount_str)
        except ValueError:
            return False, "Amount must be a valid number."

        new_expense = {
            "date": date.today().strftime("%Y-%m-%d"),
            "category": category,
            "description": description,
            "amount": amount_float
        }
        
        # Insert at the beginning so the newest items show up first in the UI
        self.expenses.insert(0, new_expense)
        StorageManager.save_data(self.expenses)
        
        return True, "Expense added successfully."

    def get_all_expenses(self):
        return self.expenses

    def get_total_balance(self):
        return sum(item['amount'] for item in self.expenses)

    def get_current_month_total(self):
        current_month = date.today().strftime("%Y-%m")
        return sum(item['amount'] for item in self.expenses if item['date'].startswith(current_month))

    def export_data(self):
        return StorageManager.export_csv(self.expenses)