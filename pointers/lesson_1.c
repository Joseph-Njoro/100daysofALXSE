#include <stdio.h>
int x = 10;
int *ptr = &x;
int y = *ptr; // Assigns the value of x (10) to y
printf("Y: %d\n",y)