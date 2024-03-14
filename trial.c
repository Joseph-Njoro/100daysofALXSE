#include <stdio.h>

int add (int, int);

int main ()
{
    int a=8, b=8, z;

    z=add(a,b);
    printf("z: %d", z);

    return 0;
}

int add(int a, int b){
    int c=a+b;
    return c;
}