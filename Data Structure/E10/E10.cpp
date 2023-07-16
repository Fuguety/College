#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Student {
public:
    string name;
    int student_id;
    double gpa;
    Student* next;

    Student(string name, int student_id, double gpa) {
        this->name = name;
        this->student_id = student_id;
        this->gpa = gpa;
        this->next = nullptr;
    }
};

class HashTable {
private:
    vector<Student*> table;
    int size;

public:
    HashTable(int size) {
        this->size = size;
        this->table = vector<Student*>(size, nullptr);
    }

    int hash(int key) {
        return key % size;
    }

    Student* get(int key) {
        int index = hash(key);
        Student* student = table[index];
        while (student != nullptr) {
            if (student->student_id == key) {
                return student;
            }
            student = student->next;
        }
        return nullptr;
    }

    void set(string name, int student_id, double gpa) {
        Student* student = get(student_id);
        if (student != nullptr) {
            student->name = name;
            student->gpa = gpa;
        } else {
            int index = hash(student_id);
            Student* new_student = new Student(name, student_id, gpa);
            new_student->next = table[index];
            table[index] = new_student;
        }
    }

    void remove(int key) {
        int index = hash(key);
        Student* student = table[index];
        Student* prev_student = nullptr;
        while (student != nullptr) {
            if (student->student_id == key) {
                if (prev_student == nullptr) {
                    table[index] = student->next;
                } else {
                    prev_student->next = student->next;
                }
                delete student;
                return;
            }
            prev_student = student;
            student = student->next;
        }
    }

    string toString() {
        string result = "";
        for (Student* student : table) {
            while (student != nullptr) {
                result += "Name: " + student->name + ", Student ID: " + to_string(student->student_id) + ", GPA: " + to_string(student->gpa) + "\n";
                student = student->next;
            }
        }
        return result;
    }
};

int main() {
    HashTable hash_table(10);
    hash_table.set("Alice", 555, 8.5);
    hash_table.set("Bob", 456, 7.8);
    hash_table.set("Charlie", 789, 9.2);

    Student* student1 = hash_table.get(555);
    if (student1 != nullptr) {
        cout << "Name: " << student1->name << ", Student ID: " << student1->student_id << ", GPA: " << student1->gpa << endl;
    }

    Student* student2 = hash_table.get(456);
    if (student2 != nullptr) {
        cout << "Name: " << student2->name << endl;
    }

    hash_table.remove(555);

    Student* student3 = hash_table.get(555);
    if (student3 != nullptr) {
        cout << "Name: " << student3->name << endl;
    }

    cout << hash_table.toString() << endl;

    return 0;
}
