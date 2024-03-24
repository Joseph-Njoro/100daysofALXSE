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
    newNode->data = value
    newNode->next = head;
    return newNode;
}

// Function to delete a node with a given value from the list
Node* deleteNode(Node head, int value) {
    if (head == NULL) {
        return NULL;
    }

    if (head->data == value) {
        Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    Node* current = head;
    while (current->next != NULL) {
        if (current->next->data == value) {
            Node* temp = current->next;
            current->next = current->next->next;
            free(temp);
            return head;
        }
        current = current->next;
    }
    return head;
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

    // Display the list before deletion
    printf("List before deletion: ");
    displayList(head);

    // Delete a node with value 2
    head = deleteNode(head, 2);

    // Display the list after deletion
    printf('List after deletion: ");
    displayList(head);

    return 0;
}