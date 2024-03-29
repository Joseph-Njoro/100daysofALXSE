#include <stdio.h>

struct Shape {
    int type;  // 0: Circle, 1: Rectangle, 2: Triangle
    union Properties {
        struct {
            float radius;
        } circle;
        struct {
            float width;
            float height;
        } rectangle;
        struct {
            float base;
            float height;
        } triangle;
    } properties;
};

int main() {
    struct Shape circle = {0, {.circle.radius = 5}};
    struct Shape rectangle = {1, {.rectangle.width = 4, .rectangle.height = 3}};
    struct Shape triangle = {2, {.triangle.base = 3, .triangle.height = 4}};

    printf("Circle: Radius = 2f\n", circle.properties.circle.radius);
    printf("Rectangle: Width = %.2f, Height = %.2f\n", rectangle.properties.rectangle.width, rectangle.properties.rectangle.height);
    printf("Triangle: Base = %.2f, Height = %2f\n", triangle.properties.triangle.base, triangle.properties.triangle.height);

    return 0;
}