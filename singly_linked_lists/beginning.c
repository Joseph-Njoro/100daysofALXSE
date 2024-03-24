#include <stdio.h>
#include <stdlib.h>

// Define a structure for a node in the singly linked list
typedef struct Node {
    int data;           // Data stored in the node
    struct Node* next;  // Pointer to the next node
} Node;

// Function to insert a new node at the beginning of the list
Node* insertBeginning(Node* head, int value) {
    Node* newNode = (Node)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = head;
    return newNode;
}

// Function to display the elements of the list
void displayList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;

    // Insert nodes at the beginning
    head = insertBeginning(head, 3);
    head = insertBeginning(head, 2);
    head = insertBeginning(head, 1);

    // Display the list
    printf("List after insertion at the beginning: ");
    displayList(head);

    return 0;
