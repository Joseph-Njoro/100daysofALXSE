#include <stdio.h>
#include <stdlib.h>

// Define a structure for a node in the singly linked list
typedef struct Node {
    int data;           // Data stored in the node
    struct Node* next;  // Pointer to the next node
} Node;

// Function to insert a new node at the beginning of the list
Node* insertBeginning(Node* head, int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = head;
    return newNode;
}

// Function to search for a node with a given value in the list
Node* searchNode(Node* head, int value) {
    Node* current = head;
    while (current != NULL) {
        if (current->data == value) {
            return current;
        }
        current = current->next;
    }
    return NULL;
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
    printf("List: ");
    displayList(head);

    // Search for a node with value 2
    int searchValue = 2;
    Node* foundNode = searchNode(head, searchValue);
    if (foundNode != NULL) {
        printf("Node with value %d found at address %p\n", searchValue, (void*)foundNode);
    } else {
        printf("Node with value %d not found in the list\n", searchValue);
    }

    return 0;
}