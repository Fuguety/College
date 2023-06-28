class ArrayQueue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.start = 0
        self.array = [0] * size

    def enqueue(self, value):
        if self.count == self.size:
            raise Exception("Queue is full")
        self.array[(self.start + self.count) % self.size] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        element = self.array[self.start]
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return element

    def is_empty(self):
        return self.count == 0

    def reset(self):
        self.count = 0
        self.start = 0

    def to_string(self):
        elements = [str(self.array[(self.start + i) % self.size]) for i in range(self.count)]
        return " ".join(elements)
    
    
    def concatenate(self, queue2):
        if not isinstance(queue2, ArrayQueue):
            raise TypeError("Parameter queue2 must be of type ArrayQueue")
        new_size = self.count + queue2.count
        if new_size > self.size:
            raise Exception("New size exceeds capacity")
        new_queue = ArrayQueue(self.size)
        for i in range(self.count):
            new_queue.enqueue(self.array[(self.start + i) % self.size])
        for i in range(queue2.count):
            new_queue.enqueue(queue2.array[(queue2.start + i) % queue2.size])
        return new_queue

    def merge(self, queue2):
        if not isinstance(queue2, ArrayQueue):
            raise TypeError("Parameter queue2 must be of type ArrayQueue")
        new_size = self.count + queue2.count
        if new_size > self.size:
            raise Exception("New size exceeds capacity")
        new_queue = ArrayQueue(self.size)
        i, j = 0, 0
        while i < self.count and j < queue2.count:
            new_queue.enqueue(self.array[(self.start + i) % self.size])
            new_queue.enqueue(queue2.array[(queue2.start + j) % queue2.size])
            i += 1
            j += 1
        while i < self.count:
            new_queue.enqueue(self.array[(self.start + i) % self.size])
            i += 1
        while j < queue2.count:
            new_queue.enqueue(queue2.array[(queue2.start + j) % queue2.size])
            j += 1
        return new_queue


def main():
    queue = ArrayQueue(5)
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(5)
    print(queue.to_string())  # Output: 3 1 5
    print(queue.dequeue())  # Output: 3
    print(queue.to_string())  # Output: 1 5
    print(queue.is_empty())  # Output: False
    queue.reset()
    print(queue.is_empty())  # Output: True




if __name__== "__main__":
    main()