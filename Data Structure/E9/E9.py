class BinaryTreeNode:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def setInfo(self, info):
        self.info = info

    def getInfo(self):
        return self.info

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setRight(self, right):
        self.right = right

    def getRight(self):
        return self.right

    def __str__(self):
        return str(self.info)







class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, v):
        return self.search_recursive(self.root, v)

    def search_recursive(self, node, v):
        if node is None or v == node.getInfo():
            return node

        if v < node.getInfo():
            return self.search_recursive(node.getLeft(), v)
        else:
            return self.search_recursive(node.getRight(), v)

    def insert(self, v):
        self.root = self.insert_recursive(self.root, v)

    def insert_recursive(self, node, v):
        if node is None:
            return BinaryTreeNode(v)

        if v < node.getInfo():
            node.setLeft(self.insert_recursive(node.getLeft(), v))
        else:
            node.setRight(self.insert_recursive(node.getRight(), v))

        return node

    def remove(self, v):
        self.root = self.remove_recursive(self.root, v)

    def remove_recursive(self, node, v):
        if node is None:
            return node

        if v < node.getInfo():
            node.setLeft(self.remove_recursive(node.getLeft(), v))
        elif v > node.getInfo():
            node.setRight(self.remove_recursive(node.getRight(), v))
        else:
            if node.getLeft() is None:
                return node.getRight()
            elif node.getRight() is None:
                return node.getLeft()

            temp = self.minimum(node.getRight())
            node.setInfo(temp.getInfo())
            node.setRight(self.remove_recursive(node.getRight(), temp.getInfo()))

        return node

    def minimum(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()
        return node

    def toString(self):
        return self.in_order(self.root)

    def in_order(self, node):
        if node is None:
            return ""

        result = self.in_order(node.getLeft())
        result += str(node.getInfo()) + " "
        result += self.in_order(node.getRight())

        return result.strip()

    def toStringDescending(self):
        return self.in_order_descending(self.root)

    def in_order_descending(self, node):
        if node is None:
            return ""

        result = self.in_order_descending(node.getRight())
        result += str(node.getInfo()) + " "
        result += self.in_order_descending(node.getLeft())

        return result.strip()

    def sumLeaves(self):
        return self.sum_leaves_recursive(self.root)

    def sum_leaves_recursive(self, node):
        if node is None:
            return 0

        if node.getLeft() is None and node.getRight() is None:
            return node.getInfo()

        return self.sum_leaves_recursive(node.getLeft()) + self.sum_leaves_recursive(node.getRight())

    def greaterThanX(self, x):
        return self.greater_than_x_recursive(self.root, x)

    def greater_than_x_recursive(self, node, x):
        if node is None:
            return 0

        if node.getInfo() > x:
            return 1 + self.greater_than_x_recursive(node.getLeft(), x) + self.greater_than_x_recursive(node.getRight(), x)
        else:
            return self.greater_than_x_recursive(node.getRight(), x)



def main():
    tree = BinarySearchTree()

    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)

    print("Tree in ascending order:")
    print(tree.toString())

    print("\nTree in descending order:")
    print(tree.toStringDescending())

    search_value = 6
    node = tree.search(search_value)
    if node is not None:
        print(f"\nElement {search_value} found in the tree.")
    else:
        print(f"\nElement {search_value} not found in the tree.")

    remove_value = 4
    tree.remove(remove_value)
    print("\nTree after removing element 4:")
    print(tree.toString())

    sum_leaves = tree.sumLeaves()
    print("\nSum of leaf node values in the tree:", sum_leaves)

    x = 7
    greater_than_x = tree.greaterThanX(x)
    print(f"\nNumber of elements greater than {x} in the tree:", greater_than_x)
    
if __name__== "__main__":
    main()
