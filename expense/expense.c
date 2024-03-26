#include <stdio,h>

// Define structures to represent expenses
typedef struct {
    int day;
    int month;
    int year;
    char category[50];
    float amount;
    char description[100]
} Expense;

// Function to add an expense
void addExpense(Expense *expenses, int numExpenses) {
    // Prompt user for expense details and store them in the expenses array
}

// Function to view all expenses
void viewExpenses(Expense *expenses, int numExpenses) {
    // Display all expenses stored in the expenses array
}

// Main function
int main() {
    Expense expenses[100]; // Array to store expenses
    int numExpenses = 0;   // Number of expenses

    // Main menu loop
    int choice;
    do {
        printf("\n Expense Tracker\n");
        printf("1. Add Expense\n");
        printf("2. View Expenses\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addExpense(expenses, numExpenses);
                break;
            case 2:
                viewExpenses(expenses, numExpenses);
                break;
            case 3:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}