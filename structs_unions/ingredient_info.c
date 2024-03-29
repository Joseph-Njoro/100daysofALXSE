#include <stdio.h>

struct Ingredient {
    char name[50];
    union Measurement {
        float quantity;
        char unit[10];
    } measurement;
};

int main() {
    struct Ingredient ingredient1 = {"Flour", {.quantity = 2.5}};
    struct Ingredient ingredient2 = {"Sugar", {.unit = "cups"}};

    printf("Ingredient 1: Name = %s, Quantity = %.2f\n", ingredient1.name, ingredient1.measurement.quantity);
    printf("Ingredient 2: Name = %s, Unit = %s\n", ingredient2.name, ingredient2.measurement.unit);

    return 0;
}