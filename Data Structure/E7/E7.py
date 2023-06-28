class TreeNode:
    def __init__(self, info):
        self.info = info
        self.first_child = None
        self.next_sibling = None
    
    def set_info(self, info):
        self.info = info
    
    def get_info(self):
        return self.info
    
    def set_first_child(self, first_child):
        self.first_child = first_child
    
    def get_first_child(self):
        return self.first_child
    
    def set_next_sibling(self, next_sibling):
        self.next_sibling = next_sibling
    
    def get_next_sibling(self):
        return self.next_sibling
    
    def to_string(self):
        return str(self.info)


class Tree:
    def __init__(self):
        self.root = None
    
    def create_node(self, info):
        return TreeNode(info)
    
    def insert_child(self, parent_node, child_node):
        if parent_node.get_first_child() is None:
            parent_node.set_first_child(child_node)
        else:
            current = parent_node.get_first_child()
            while current.get_next_sibling() is not None:
                current = current.get_next_sibling()
            current.set_next_sibling(child_node)
    
    def to_string(self):
        if self.root is not None:
            return self.print_tree(self.root, 0)
        else:
            return "Empty tree."
    
    def print_tree(self, node, level):
        result = "  " * level + node.to_string() + "\n"
        if node.get_first_child() is not None:
            current = node.get_first_child()
            while current is not None:
                result += self.print_tree(current, level + 1)
                current = current.get_next_sibling()
        return result
    
    def contains(self, info):
        return self.contains_aux(self.root, info)
    
    def contains_aux(self, node, info):
        if node is None:
            return False
        if node.get_info() == info:
            return True
        current = node.get_first_child()
        while current is not None:
            if self.contains_aux(current, info):
                return True
            current = current.get_next_sibling()
        return False
    
    def height(self):
        return self.height_aux(self.root)
    
    def height_aux(self, node):
        if node is None:
            return 0
        max_height = 0
        current = node.get_first_child()
        while current is not None:
            child_height = self.height_aux(current)
            max_height = max(max_height, child_height)
            current = current.get_next_sibling()
        return 1 + max_height
    
    def count_even_numbers(self):
        return self.count_even_numbers_aux(self.root)
    
    def count_even_numbers_aux(self, node):
        if node is None:
            return 0
        count = 0
        if node.get_info() % 2 == 0:
            count += 1
        current = node.get_first_child()
        while current is not None:
            count += self.count_even_numbers_aux(current)
            current = current.get_next_sibling()
        return count
    
    def count_leaf_nodes(self):
        return self.count_leaf_nodes_aux(self.root)
    
    def count_leaf_nodes_aux(self, node):
        if node is None:
            return 0
        if node.get_first_child() is None:
            return 1
        count = 0
        current = node.get_first_child()
        while current is not None:
            count += self.count_leaf_nodes_aux(current)
            current = current.get_next_sibling()
        return count
    
    def is_equal(self, other_tree):
        return self.is_equal_aux(self.root, other_tree.root)
    
    def is_equal_aux(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.get_info() != node2.get_info():
            return False
        current1 = node1.get_first_child()
        current2 = node2.get_first_child()
        while current1 is not None and current2 is not None:
            if not self.is_equal_aux(current1, current2):
                return False
            current1 = current1.get_next_sibling()
            current2 = current2.get_next_sibling()
        return current1 is None and current2 is None
    
    def copy(self):
        new_tree = Tree()
        new_tree.root = self.copy_aux(self.root)
        return new_tree
    
    def copy_aux(self, node):
        if node is None:
            return None
        new_node = TreeNode(node.get_info())
        current = node.get_first_child()
        while current is not None:
            new_child = self.copy_aux(current)
            if new_node.get_first_child() is None:
                new_node.set_first_child(new_child)
            else:
                temp = new_node.get_first_child()
                while temp.get_next_sibling() is not None:
                    temp = temp.get_next_sibling()
                temp.set_next_sibling(new_child)
            current = current.get_next_sibling()
        return new_node


def main():
    # Create an empty tree
    tree = Tree()

    # Create nodes
    node1 = tree.create_node(1)
    node2 = tree.create_node(2)
    node3 = tree.create_node(3)
    node4 = tree.create_node(4)
    node5 = tree.create_node(5)
    node6 = tree.create_node(6)
    node7 = tree.create_node(7)
    node8 = tree.create_node(8)

    # Build the tree structure
    tree.insert_child(node1, node2)
    tree.insert_child(node1, node3)
    tree.insert_child(node1, node4)
    tree.insert_child(node2, node5)
    tree.insert_child(node3, node6)
    tree.insert_child(node4, node7)
    tree.insert_child(node4, node8)

    # Print the tree structure
    print(tree.to_string())

    # Check if certain values belong to the tree
    print("Belongs to tree:", tree.contains(3))
    print("Belongs to tree:", tree.contains(9))

    # Calculate the height of the tree
    print("Tree height:", tree.height())

    # Count the number of even numbers in the tree
    print("Number of even numbers:", tree.count_even_numbers())

    # Count the number of leaf nodes in the tree
    print("Number of leaf nodes:", tree.count_leaf_nodes())

    # Create a copy of the tree
    tree_copy = tree.copy()

    # Check if the copied tree is equal to the original tree
    print("Trees are equal:", tree.is_equal(tree_copy))


if __name__ == '__main__':
    main()
