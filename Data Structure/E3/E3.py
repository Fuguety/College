class NoLista:
    def __init__(self, info):
        self.info = info
        self.next = None

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class Lista:
    def __init__(self):
        self.first = None

    def insert(self, v):
        new_node = NoLista(v)
        if self.is_empty():
            self.first = new_node
        else:
            current = self.first
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def print_list(self):
        current = self.first
        while current is not None:
            print(current.get_info(), end=' ')
            current = current.get_next()
        print()

    def is_empty(self):
        return self.first is None

    def search(self, v):
        current = self.first
        while current is not None:
            if current.get_info() == v:
                return current
            current = current.get_next()
        return None

    def length(self):
        count = 0
        current = self.first
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

    def remove(self, v):
        if self.is_empty():
            return
        if self.first.get_info() == v:
            self.first = self.first.get_next()
            return
        previous = self.first
        current = self.first.get_next()
        while current is not None:
            if current.get_info() == v:
                previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()

    def clear(self):
        self.first = None

    def insert_end(self, v):
        new_node = NoLista(v)
        if self.is_empty():
            self.first = new_node
        else:
            last_node = self.last()
            last_node.set_next(new_node)

    def is_equal(self, l):
        current1 = self.first
        current2 = l.first
        while current1 is not None and current2 is not None:
            if current1.get_info() != current2.get_info():
                return False
            current1 = current1.get_next()
            current2 = current2.get_next()
        return current1 is None and current2 is None

    def print_recursive(self):
        self.print_recursive_aux(self.first)
        print()

    def print_recursive_aux(self, node):
        if node is None:
            return
        print(node.get_info(), end=' ')
        self.print_recursive_aux(node.get_next())

    def remove_recursive(self, v):
        self.first = self.remove_recursive_aux(self.first, v)

    def remove_recursive_aux(self, node, v):
        if node is None:
            return None
        if node.get_info() == v:
            return node.get_next()
        node.set_next(self.remove_recursive_aux(node.get_next(), v))
        return node

def main():
    # Example usage
    list_obj = Lista()
    list_obj.insert(1)
    list_obj.insert(2)
    list_obj.insert(3)
    list_obj.print_list()  # Output: 1 2 3

    list_obj.remove(2)
    list_obj.print_list()  # Output: 1 3

if __name__== "__main__":
    main()