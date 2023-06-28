class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.first = None

    def insert(self, value):
        new_node = ListNode(value)
        new_node.set_next(self.first)
        self.first = new_node

    def print_list(self):
        current = self.first
        while current is not None:
            print(current.get_value())
            current = current.get_next()

    def __str__(self):
        list_str = ""
        current = self.first
        while current is not None:
            list_str += str(current.get_value()) + " "
            current = current.get_next()
        return list_str

    def is_empty(self):
        return self.first is None

    def search(self, value):
        current = self.first
        while current is not None:
            if current.get_value() == value:
                return current
            current = current.get_next()
        return None

    def length(self):
        current = self.first
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def last(self):
        current = self.first
        if current is None:
            return None
        while current.get_next() is not None:
            current = current.get_next()
        return current


def main():
    # Testing the implemented list
    linked_list = LinkedList()

    # Testing insert() method
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    linked_list.insert(20)

    # Testing print_list() method
    linked_list.print_list()

    # Testing __str__() method
    print(str(linked_list))

    # Testing is_empty() method
    print(linked_list.is_empty())

    # Testing search() method
    found_node = linked_list.search(25)
    if found_node is not None:
        print("Node found:", found_node.get_value())
    else:
        print("Node not found")

    # Testing length() method
    print("Length of the list:", linked_list.length())

    # Testing last() method
    last_node = linked_list.last()
    if last_node is not None:
        print("Last node:", last_node.get_value())
    else:
        print("The list is empty")
        
if __name__== "__main__":
    main()
