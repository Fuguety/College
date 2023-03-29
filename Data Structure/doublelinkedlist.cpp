#include <iostream>

using namespace std;


struct Node {
    int data;
    Node* prev;
    Node* next;
};

void addNode(Node** head, int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = (*head);

    if ((*head) != NULL) {
        (*head)->prev = newNode;
    }

    (*head) = newNode;
}


void printList(Node* node) {
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}


int main() {
    Node* head = NULL;

    addNode(&head, 1);
    addNode(&head, 2);
    addNode(&head, 3);
    addNode(&head, 4);
    addNode(&head, 5);

    cout << "Lista: ";
    printList(head);

    return 0;
}
