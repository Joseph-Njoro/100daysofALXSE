#include <stdio.h>
#include <stdlib.h>

// define a struct for the linked list
typedef struct {
    int data;
    struct node* next;
} node;

int main() {
    // create a new node
    node *new_node;
    new_node = (node*) malloc(sizeof(node));
    if (new_node == NULL) {
        printf("Memory not allocated");
        exit(0);
    }

    // assign values to the node
    new_node->data = 10;
    new_node->next = NULL;

    // add more nodes to the linked list
    node *head = new_node;
    node *current = new_node;

    for (int i = 2; i <= 5; i++) {
        node *new_node = (node*) malloc(sizeof(node));
        if (new_node == NULL) {
            printf("Memory not allocated");
            exit(0);
        }

        new_node->data = i;
        new_node->next = NULL;

        current->next = new_node;
        current = new_node;
    }

    // print the linked list
    current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }

    // free the memory
    current = head;
    while (current != NULL) {
        node *next = current->next;
        free(current);
        current = next;
    }

    return 0;
}