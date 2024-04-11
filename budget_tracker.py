import pandas as pd

class BudgetTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])

    def add_transaction(self, date, description, category, amount):
        self.transactions = self.transactions.append({'Date': date,
                                                       'Description': description,
                                                       'Category': category,
                                                       'Amount': amount}, ignore_index=True)

    def view_transactions(self):
        return self.transactions

    def view_summary(self):
        summary = self.transactions.groupby('Category')['Amount'].sum()
        return summary

# Sample usage
if __name__ == "__main__":
    budget_tracker = BudgetTracker()

    # Adding transactions
    budget_tracker.add_transaction('2024-04-11', 'Salary', 'Income', 3000)
    budget_tracker.add_transaction('2024-04-11', 'Rent', 'Housing', -1000)
    budget_tracker.add_transaction('2024-04-12', 'Groceries', 'Food', -200)
    budget_tracker.add_transaction('2024-04-12', 'Internet Bill', 'Utilities', -50)

    # Viewing transactions and summary
    print("All Transactions:")
    print(budget_tracker.view_transactions())
    print("\nSummary by Category:")
    print(budget_tracker.view_summary())