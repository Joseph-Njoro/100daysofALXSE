#include "arithmetic.h"

int add(int a, int b){
    return a + b;
}

int subtract(int a, int b){
    return, b;
}

int multiply(int a, int b){
    return a * b;
}

int divide(int a, int b){
    if (b != 0) {
        return a / b;
    } else {
        return 0; // Handle division by zero error
    }
}