#include <iostream>
using namespace std;


class NoLista {
private:
    int info;
    NoLista* next;

public:
    NoLista(int info) {
        this->info = info;
        this->next = nullptr;
    }

    void set_info(int info) {
        this->info = info;
    }

    int get_info() const {
        return info;
    }

    void set_next(NoLista* next) {
        this->next = next;
    }

    NoLista* get_next() const {
        return next;
    }
};

class Lista {
private:
    NoLista* first;

public:
    Lista() {
        this->first = nullptr;
    }

    void insert(int v) {
        NoLista* new_node = new NoLista(v);
        if (is_empty()) {
            first = new_node;
        }
        else {
            NoLista* current = first;
            while (current->get_next() != nullptr) {
                current = current->get_next();
            }
            current->set_next(new_node);
        }
    }

    void print_list() const {
        NoLista* current = first;
        while (current != nullptr) {
            std::cout << current->get_info() << ' ';
            current = current->get_next();
        }
        std::cout << std::endl;
    }

    bool is_empty() const {
        return first == nullptr;
    }

    NoLista* search(int v) const {
        NoLista* current = first;
        while (current != nullptr) {
            if (current->get_info() == v) {
                return current;
            }
            current = current->get_next();
        }
        return nullptr;
    }

    int length() const {
        int count = 0;
        NoLista* current = first;
        while (current != nullptr) {
            count += 1;
            current = current->get_next();
        }
        return count;
    }

    NoLista* last() const {
        NoLista* current = first;
        if (current == nullptr) {
            return nullptr;
        }
        while (current->get_next() != nullptr) {
            current = current->get_next();
        }
        return current;
    }

    void remove(int v) {
        if (is_empty()) {
            return;
        }
        if (first->get_info() == v) {
            NoLista* temp = first;
            first = first->get_next();
            delete temp;
            return;
        }
        NoLista* previous = first;
        NoLista* current = first->get_next();
        while (current != nullptr) {
            if (current->get_info() == v) {
                previous->set_next(current->get_next());
                delete current;
                return;
            }
            previous = current;
            current = current->get_next();
        }
    }

    void clear() {
        NoLista* current = first;
        while (current != nullptr) {
            NoLista* temp = current;
            current = current->get_next();
            delete temp;
        }
        first = nullptr;
    }

    void insert_end(int v) {
        NoLista* new_node = new NoLista(v);
        if (is_empty()) {
            first = new_node;
        }
        else {
            NoLista* last_node = last();
            last_node->set_next(new_node);
        }
    }

    bool is_equal(const Lista& l) const {
        NoLista* current1 = first;
        NoLista* current2 = l.first;
        while (current1 != nullptr && current2 != nullptr) {
            if (current1->get_info() != current2->get_info()) {
                return false;
            }
            current1 = current1->get_next();
            current2 = current2->get_next();
        }
        return current1 == nullptr && current2 == nullptr;
    }

    void print_recursive() const {
        print_recursive_aux(first);
        std::cout << std::endl;
    }

    void print_recursive_aux(NoLista* node) const {
        if (node == nullptr) {
            return;
        }
        std::cout << node->get_info() << ' ';
        print_recursive_aux(node->get_next());
    }

    void remove_recursive(int v) {
        first = remove_recursive_aux(first, v);
    }

    NoLista* remove_recursive_aux(NoLista* node, int v) {
        if (node == nullptr) {
            return nullptr;
        }
        if (node->get_info() == v) {
            NoLista* next_node = node->get_next();
            delete node;
            return next_node;
        }
        node->set_next(remove_recursive_aux(node->get_next(), v));
        return node;
    }
};

int main() {
    // Example usage
    Lista list_obj;
    list_obj.insert(1);
    list_obj.insert(2);
    list_obj.insert(3);
    list_obj.print_list();  // Output: 1 2 3

    list_obj.remove(2);
    list_obj.print_list();  // Output: 1 3

    return 0;
}
