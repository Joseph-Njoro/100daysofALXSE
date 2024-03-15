#include <stdio.h>

void greet(char a[1]);

int main()
{
    char a[100];
    printf("Enter a name: ");
    scanf("%s", a);
    greet(a);
    return 0;
}

void greet(char a[]){
    printf("Hi %s\n", &a);
}