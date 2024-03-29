#include <stdio.h>

struct Vehicle {
    char make_model[50];
    int year;
    union Details {
        float engine_size;
        int seating_capacity;
    } details;
};

int main() {
    struct Vehicle car = {"Toyota Camry", 2022, {.engine_size = 2.5}};
    struct Vehicle van = {"Ford Transit", 2019, {.seating_capacity = 8}};

    printf("Car: Make/Model = %s, Year = %d, Engine Size = %.2f\n", car.make_model, car.year, car.details.engine_size);
    printf("Van: Make/Model = %s, Year = %d, Seating Capacity = %d\n", van.make_model, van.year, van.details.seating_capacity);

    return 0;
}