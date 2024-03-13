#include <stdio.h>

int main(void){
    int age;
    printf("Enter your age\n");
    scanf("%d",&age);
    if (age < 18){
        printf("You are too young");
    }else if(age<=30){
        printf("Hey young man");
    }else if(age<=50){
        printf("Hi Mr, lets proceed");
    }else{
        printf("Use a secure password");
    }
    return 0;
}