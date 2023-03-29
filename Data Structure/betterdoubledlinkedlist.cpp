#include <iostream>

using namespace std;

class List {
    private:
        struct Node {
            int data;
            Node* prev;
            Node* next;
        };
        
        Node* head = NULL;

    public:
        void addNode(int data) {
            Node* newNode = new Node();
            newNode->data = data;
            newNode->prev = NULL;
            newNode->next = head;

            if (head != NULL) {
                head->prev = newNode;
            }

            head = newNode;
        }

        void addNodeAtEnd(int data) {
            Node* newNode = new Node();
            newNode->data = data;
            newNode->next = NULL;

            if (head == NULL) {
                newNode->prev = NULL;
                head = newNode;
                return;
            }

            Node* lastNode = head;
            while (lastNode->next != NULL) {
                lastNode = lastNode->next;
            }

            lastNode->next = newNode;
            newNode->prev = lastNode;
        }

        Node* getLastNode() {
            Node* node = head;
            while (node != NULL && node->next != NULL) {
                node = node->next;
            }
            return node;
        }

        void clearList() {
            Node* current = head;
            Node* next = NULL;

            while (current != NULL) {
                next = current->next;
                delete current;
                current = next;
            }

            head = NULL;
        }

        int length() {
            int count = 0;
            Node* node = head;
            while (node != NULL) {
                count++;
                node = node->next;
            }
            return count;
        }

        Node* search(int value) {
            Node* node = head;
            while (node != NULL) {
                if (node->data == value) {
                    return node;
                }
                node = node->next;
            }
            return NULL;
        }

        void printList() {
            Node* node = head;
            while (node != NULL) {
                cout << node->data << " ";
                node = node->next;
            }
            cout << endl;
        }
};

int main() {
    List list;

    list.addNode(1);
    list.addNode(2);
    list.addNode(3);
    list.addNode(4);
    list.addNode(5);

    cout << "List: ";
    list.printList();

    list.addNodeAtEnd(6);
    cout << "List after inserting 6 at the end: ";
    list.printList();

    List::Node* lastNode = list.getLastNode();
    cout << "Last term: " << lastNode->data << endl;

    list.clearList();
    cout << "List is now empty: ";
    list.printList();

    list.addNode(1);
    list.addNode(2);
    list.addNode(3);
    list.addNode(4);
    list.addNode(5);
    cout << "Lenght of the list: " << list.length() << endl;

    List::Node* node = list.search(3);
    if (node != NULL) {
        cout << "Node with value 3 found" << endl;
    } else {
        cout << "Node with value 3 not found" << endl;
    }

    return 0;
}
