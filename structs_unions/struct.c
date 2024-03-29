#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p1;

    p1.x = 10;
    p1.y = 20;

    printf("Point coordinates: (%d %d)\n", p1.x, p1.y);

    return 0;
}