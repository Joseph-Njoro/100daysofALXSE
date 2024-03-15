#include <stdio.h>

void greet(char a[]);

int main(){
    char[] a;
    printf("Enter a name");
    scanf("%s", &a);
    greet(a);
    return 0;
}

void greet(char a){
    printf("Hi %s\n", &a);
}