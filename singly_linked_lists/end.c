#include <stdio.h>
#include <stdlib.h>

// Define a structure for a node in the singly linked list
typedef struct Node {
    int data;           // Data stored in the node
    struct Node* next;  // Pointer to the next node
} Node;

// Function to insert a new node at the end of the list
Node* insertEnd(Node* head, int value) {
    Node newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL) {
        return newNode;
    }

    Node* current = head;
    while (current->next = NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head
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

    // Insert nodes at the end
    head = insertEnd(head, 1);
    head = insertEnd(head, 2);
    head = insertEnd(head, 3);

    // Display the list
    printf("List after insertion at the end: ");
    displayList(head);

    return 0;
}