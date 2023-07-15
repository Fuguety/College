#include <iostream>

using namespace std;

class ListNode {
private:
    int value;
    ListNode* next;

public:
    ListNode(int value) {
        this->value = value;
        next = nullptr;
    }

    int getValue() {
        return value;
    }

    void setValue(int value) {
        this->value = value;
    }

    ListNode* getNext() {
        return next;
    }

    void setNext(ListNode* nextNode) {
        next = nextNode;
    }
};

class LinkedList {
private:
    ListNode* first;

public:
    LinkedList() {
        first = nullptr;
    }

    void insert(int value) {
        ListNode* newNode = new ListNode(value);
        newNode->setNext(first);
        first = newNode;
    }

    void printList() {
        ListNode* current = first;
        while (current != nullptr) {
            cout << current->getValue() << endl;
            current = current->getNext();
        }
    }

    string toString() {
        string listStr = "";
        ListNode* current = first;
        while (current != nullptr) {
            listStr += to_string(current->getValue()) + " ";
            current = current->getNext();
        }
        return listStr;
    }

    bool isEmpty() {
        return first == nullptr;
    }

    ListNode* search(int value) {
        ListNode* current = first;
        while (current != nullptr) {
            if (current->getValue() == value) {
                return current;
            }
            current = current->getNext();
        }
        return nullptr;
    }

    int length() {
        ListNode* current = first;
        int count = 0;
        while (current != nullptr) {
            count++;
            current = current->getNext();
        }
        return count;
    }

    ListNode* last() {
        ListNode* current = first;
        if (current == nullptr) {
            return nullptr;
        }
        while (current->getNext() != nullptr) {
            current = current->getNext();
        }
        return current;
    }
};

int main() {
    // Testing the implemented list
    LinkedList linkedList;

    // Testing insert() method
    linkedList.insert(5);
    linkedList.insert(10);
    linkedList.insert(15);
    linkedList.insert(20);

    // Testing printList() method
    linkedList.printList();

    // Testing toString() method
    cout << linkedList.toString() << endl;

    // Testing isEmpty() method
    cout << linkedList.isEmpty() << endl;

    // Testing search() method
    ListNode* foundNode = linkedList.search(25);
    if (foundNode != nullptr) {
        cout << "Node found: " << foundNode->getValue() << endl;
    } else {
        cout << "Node not found" << endl;
    }

    // Testing length() method
    cout << "Length of the list: " << linkedList.length() << endl;

    // Testing last() method
    ListNode* lastNode = linkedList.last();
    if (lastNode != nullptr) {
        cout << "Last node: " << lastNode->getValue() << endl;
    } else {
        cout << "The list is empty" << endl;
    }

    return 0;
}
