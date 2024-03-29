#include <stdio.h>

struct Employee {
    char name[50];
    int emp_id;
    union Salary {
        float hourly_rate;
        float monthly_salary;
    } salary;
};

int main() {
    struct Employee employee1 = {"Alice", 1001, {.hourly_rate = 25.5}};
    struct Employee employee2 = {"Bob", 1002, {.monthly_salary = 4000}};

    printf("Employee 1: Name = %s, Employee ID = %d, Hourly Rate = %.2f\n", employee1.name, employee1.emp_id, employee1.salary.hourly_rate);
    printf("Employee 2: Name = %s, Employee ID = %d, Monthly Salary = %.2f\n", employee2.name, employee2.emp_id, employee2.salary.monthly_salary);

    return 0;
}