#include <stdio.h>

int main(void){
    int team;
    char a[]="Manchester United\n";
    char b[]="Chelsea\n";

    printf("Which ePL team do you supoort?\n ");
    printf("a = %s b = %s\n Answer: ",a ,b);

    scanf("%d", &team );

    if (team == 1 ){
        printf("Endelea kupiga mdomo %s\n",a);
    }
    else if (team == 2){
        printf("Team kubwa... @team %s\n",b);
    }
    else{
        printf("Kama wewe sio wa City ama Liverpool kalale\n");
    }
    return 0;
}