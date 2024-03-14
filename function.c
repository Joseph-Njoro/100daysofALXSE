#include <stdio.h>

int add(int, int);

int main ()
{
    int a=90,b=78,d;
    d=add(a,b);
    printf("Summation of a b & c is d. d is: %d",d);
    return 0;
}

    int add(int a,int b){
        int z=(a+b);
        return z;
    }
    