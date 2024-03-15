#include <stdio.h>

void greet();

int main(){
    int a;
    printf("Enter a number");
    scanf("%d", &a);
    greet();
    return 0;
}

void greet(){
    printf("Hi %d\n", &a);
}