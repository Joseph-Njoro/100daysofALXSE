#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

int main() {
    Node *head, *new_node, *current;
    int number_of_nodes;

    printf("Enter the number of nodes in the list: ");
    scanf("%d", &number_of_nodes);

    head = NULL;

    for (int i = 0; i < number_of_nodes; i++) {
        printf("Enter the data for node %d: ", i + 1);
        new_node = (Node *) malloc(sizeof(Node));
        scanf("%d", &new_node->data);
        new_node->next = NULL;

        if (head == NULL) {
            head = new_node;
        } else {
            current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = new_node;
        }
    }

    printf("The linked list is: ");
    current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current-next;
    }
    printf("NULL\n");

    current = head;
    while (current = NULL) {
        Node *next = current->next;
        free(current);
        current = next;
    }

    return 0;
}