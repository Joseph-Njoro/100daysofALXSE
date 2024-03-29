#include <stdio.h>

struct Account {
    char account_holder[50];
    int account_number;
    union Balance {
        float current_balance;
        float savings_balance;
    } balance;
};

int main() {
    struct Account checking = {"John Doe", 1001, {.current_balance = 2500}};
    struct Account savings = {"Jane Smith", 1002, {.savings_balance = 5000}};

    printf("Checking Account: Holder = s, Account Number = %d, Current Balance = %.2f\n", checking.account_holder, checking.account_number, checking.balance.current_balance);
    printf("Savings Account: Holder = %s, Account Number = %d, Savings Balance = %.2f\n", savings.account_holder, savings.account_number, savings.balance.savings_balance);

    return 0;
}