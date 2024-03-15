#include <stdio.h>

void greet();

int main(){
    greet();
    int a;
    scanf("%d", &a);
    return 0;
}

void greet(){
    printf("Hi %d\n", &a);
}