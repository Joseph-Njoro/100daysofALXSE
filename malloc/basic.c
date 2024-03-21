#include <stdio.h>
#include <stdlib.h>

int main() {
    // We want ptr to store the space of 3 integers
    int *ptr;
    ptr = (int*) malloc(3 * sizeof(int));

    if(ptr==NULL){
        printf("Memory not allocated. \n");
    }
    else{
        printf("Memory allocated succesfully. \n");
        // This statement shows where memory is allocated
        printf("The address of the pointer is: %u\n ", ptr);
        // Here we assign values to the ptr created
        for(int i=0;i<3;i++){
            ptr[i] = i;
        }
        // Printing the values of ptr to show memory allocation is done
        for(int i=0;i<3;i++){
            printf("%d\n", ptr[i]);
        }
    }
    return 0;
}