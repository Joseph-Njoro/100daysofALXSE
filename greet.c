#include <stdio.h>

void greet();

int main(){
    int a;
    printf("Enter a number");
    scanf("%d", &a);
    return 0;
    greet();
}

void greet(){
    printf("Hi %d\n", &a);
}