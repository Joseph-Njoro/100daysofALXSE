import pandas as pd
import tkinter as tk
from tkinter import messagebox

class BudgetTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])

    def add_transaction(self, date, description, category, amount):
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")
            return

        if amount == 0:
            messagebox.showerror("Error", "Amount cannot be zero")
            return

        if category not in ['Income', 'Housing', 'Food', 'Utilities', 'Entertainment', 'Transportation', 'Others']:
            messagebox.showerror("Error", "Invalid category")
            return

        self.transactions = self.transactions.append({'Date': date,
                                                       'Description': description,
                                                       'Category': category,
                                                       'Amount': amount}, ignore_index=True)

    def view_transactions(self):
        return self.transactions

    def view_summary(self):
        summary = self.transactions.groupby('Category')['Amount'].sum()
        return summary

# Create GUI
class BudgetTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Budget Tracker")
        self.master.configure(bg='darkblue')

        self.date_label = tk.Label(master, text="Date:", bg='darkblue', fg='white', font=('Arial', 14))
        self.date_label.grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(master, font=('Arial', 14))
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(master, text="Description:", bg='darkblue', fg='white', font=('Arial', 14))
        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(master, font=('Arial', 14))
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label = tk.Label(master, text="Category:", bg='darkblue', fg='white', font=('Arial', 14))
        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(master, font=('Arial', 14))
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        self.amount_label = tk.Label(master, text="Amount:", bg='darkblue', fg='white', font=('Arial', 14))
        self.amount_label.grid(row=3, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(master, font=('Arial', 14))
        self.amount_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Transaction", command=self.add_transaction, font=('Arial', 14))
        self.add_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.view_transactions_button = tk.Button(master, text="View Transactions", command=self.view_transactions, font=('Arial', 14))
        self.view_transactions_button.grid(row=5, columnspan=2, padx=10, pady=10)

        self.summary_button = tk.Button(master, text="View Summary", command=self.view_summary, font=('Arial', 14))
        self.summary_button.grid(row=6, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(master, text="", bg='darkblue', fg='white', font=('Arial', 14))
        self.result_label.grid(row=7, columnspan=2, padx=10, pady=10)

        self.budget_tracker = BudgetTracker()

    def add_transaction(self):
        date = self.date_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        self.budget_tracker.add_transaction(date, description, category, amount)
        self.result_label.config(text="Transaction added successfully", fg='green')

    def view_transactions(self):
        transactions = self.budget_tracker.view_transactions()
        self.result_label.config(text=transactions, fg='white')

    def view_summary(self):
        summary = self.budget_tracker.view_summary()
        self.result_label.config(text=summary, fg='white')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    app = BudgetTrackerGUI(root)
    root.mainloop()