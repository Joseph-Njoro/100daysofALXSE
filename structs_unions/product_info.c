#include <stdio.h>

struct Product {
    char name[50];
    int product_id;
    union Price {
        float unit_price;
        float bulk_price;
    } price;
};

int main() {
    struct Product product1 = {"Laptop", 1001, {.unit_price = 899.99}};
    struct Product product2 = {"Smartphone", 1002, {.bulk_price = 499.99}};

    printf("Product 1: Name = %s, Product ID = %
