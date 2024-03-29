#include <stdio.h>

union Data {
    int i;
    float f;
    char str[20]
};

int main() {
    union Data data;

    data.i = 10;
    printf("Data as integer: %d\n", data.i);

    data.f = 3.14;
    printf("Data as float: %.2f\n", data.f);

    strcpy(data.str, "Hello");
    printf("Data as string: %s\n", data.str);

    return 0;
}