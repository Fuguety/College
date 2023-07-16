#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

class ArrayQueue {
private:
    int size;
    int count;
    int start;
    vector<int> array;

public:
    ArrayQueue(int size) : size(size), count(0), start(0), array(size, 0) {}

    void enqueue(int value) {
        if (count == size)
            throw runtime_error("Queue is full");

        array[(start + count) % size] = value;
        count++;
    }

    int dequeue() {
        if (is_empty())
            throw runtime_error("Queue is empty");

        int element = array[start];
        start = (start + 1) % size;
        count--;
        return element;
    }

    bool is_empty() {
        return count == 0;
    }

    void reset() {
        count = 0;
        start = 0;
    }

    string to_string() {
        vector<string> elements(count);
        for (int i = 0; i < count; i++) {
            elements[i] = std::to_string(array[(start + i) % size]);
        }
        return accumulate(elements.begin(), elements.end(), string(" "), [](const string& a, const string& b) {
            return a + " " + b;
        });
    }

    ArrayQueue concatenate(ArrayQueue& queue2) {
        if (!is_same<decltype(queue2), ArrayQueue>::value)
            throw runtime_error("Parameter queue2 must be of type ArrayQueue");

        int new_size = count + queue2.count;
        if (new_size > size)
            throw runtime_error("New size exceeds capacity");

        ArrayQueue new_queue(size);
        for (int i = 0; i < count; i++) {
            new_queue.enqueue(array[(start + i) % size]);
        }
        for (int i = 0; i < queue2.count; i++) {
            new_queue.enqueue(queue2.array[(queue2.start + i) % queue2.size]);
        }
        return new_queue;
    }

    ArrayQueue merge(ArrayQueue& queue2) {
        if (!is_same<decltype(queue2), ArrayQueue>::value)
            throw runtime_error("Parameter queue2 must be of type ArrayQueue");

        int new_size = count + queue2.count;
        if (new_size > size)
            throw runtime_error("New size exceeds capacity");

        ArrayQueue new_queue(size);
        int i = 0, j = 0;
        while (i < count && j < queue2.count) {
            new_queue.enqueue(array[(start + i) % size]);
            new_queue.enqueue(queue2.array[(queue2.start + j) % queue2.size]);
            i++;
            j++;
        }
        while (i < count) {
            new_queue.enqueue(array[(start + i) % size]);
            i++;
        }
        while (j < queue2.count) {
            new_queue.enqueue(queue2.array[(queue2.start + j) % queue2.size]);
            j++;
        }
        return new_queue;
    }
};

void main() {
    ArrayQueue queue(5);
    queue.enqueue(3);
    queue.enqueue(1);
    queue.enqueue(5);
    cout << queue.to_string() << endl;  // Output: 3 1 5
    cout << queue.dequeue() << endl;   // Output: 3
    cout << queue.to_string() << endl;  // Output: 1 5
    cout << queue.is_empty() << endl;  // Output: False
    queue.reset();
    cout << queue.is_empty() << endl;  // Output: True
}

int main() {
    main();
    return 0;
}
