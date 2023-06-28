class BinaryTreeNode:
    def __init__(self, info: int, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def setInfo(self, info: int):
        self.info = info

    def getInfo(self) -> int:
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


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int, left, right) -> BinaryTreeNode:
        new_node = BinaryTreeNode(value, left, right)
        if self.root is None:
            self.root = new_node
        else:
            self.insertNode(self.root, new_node)
        return new_node

    def insertNode(self, current_node: BinaryTreeNode, new_node: BinaryTreeNode):
        if new_node.getInfo() < current_node.getInfo():
            if current_node.getLeft() is None:
                current_node.setLeft(new_node)
            else:
                self.insertNode(current_node.getLeft(), new_node)
        else:
            if current_node.getRight() is None:
                current_node.setRight(new_node)
            else:
                self.insertNode(current_node.getRight(), new_node)

    def isEmpty(self) -> bool:
        return self.root is None

    def toString(self) -> str:
        return self.toStringAux(self.root)

    def toStringAux(self, node: BinaryTreeNode) -> str:
        if node is None:
            return ""
        else:
            result = self.toStringAux(node.getLeft())
            result += str(node.getInfo()) + " "
            result += self.toStringAux(node.getRight())
            return result

    def contains(self, info: int) -> bool:
        return self.containsNode(self.root, info)

    def containsNode(self, node: BinaryTreeNode, info: int) -> bool:
        if node is None:
            return False
        elif info == node.getInfo():
            return True
        elif info < node.getInfo():
            return self.containsNode(node.getLeft(), info)
        else:
            return self.containsNode(node.getRight(), info)

    def countEvenNumbers(self) -> int:
        return self.countEvenNumbersNode(self.root)

    def countEvenNumbersNode(self, node: BinaryTreeNode) -> int:
        if node is None:
            return 0
        count = 0
        if node.getInfo() % 2 == 0:
            count += 1
        count += self.countEvenNumbersNode(node.getLeft())
        count += self.countEvenNumbersNode(node.getRight())
        return count

    def countLeaves(self) -> int:
        return self.countLeavesNode(self.root)

    def countLeavesNode(self, node: BinaryTreeNode) -> int:
        if node is None:
            return 0
        elif node.getLeft() is None and node.getRight() is None:
            return 1
        else:
            return self.countLeavesNode(node.getLeft()) + self.countLeavesNode(node.getRight())

    def printPreorder(self) -> str:
        return self.printPreorderAux(self.root)

    def printPreorderAux(self, node: BinaryTreeNode) -> str:
        if node is None:
            return ""
        result = str(node.getInfo()) + " "
        result += self.printPreorderAux(node.getLeft())
        result += self.printPreorderAux(node.getRight())
        return result

    def printInorder(self) -> str:
        return self.printInorderAux(self.root)

    def printInorderAux(self, node: BinaryTreeNode) -> str:
        if node is None:
            return ""
        result = self.printInorderAux(node.getLeft())
        result += str(node.getInfo()) + " "
        result += self.printInorderAux(node.getRight())
        return result

    def printPostorder(self) -> str:
        return self.printPostorderAux(self.root)

    def printPostorderAux(self, node: BinaryTreeNode) -> str:
        if node is None:
            return ""
        result = self.printPostorderAux(node.getLeft())
        result += self.printPostorderAux(node.getRight())
        result += str(node.getInfo()) + " "
        return result

    def countNodes(self) -> int:
        return self.countNodesAux(self.root)

    def countNodesAux(self, node: BinaryTreeNode) -> int:
        if node is None:
            return 0
        return 1 + self.countNodesAux(node.getLeft()) + self.countNodesAux(node.getRight())

    def getHeight(self) -> int:
        return self.getHeightAux(self.root)

    def getHeightAux(self, node: BinaryTreeNode) -> int:
        if node is None:
            return -1
        left_height = self.getHeightAux(node.getLeft())
        right_height = self.getHeightAux(node.getRight())
        return 1 + max(left_height, right_height)

    def areEqual(self, tree: 'BinaryTree') -> bool:
        return self.areEqualAux(self.root, tree.root)

    def areEqualAux(self, node1: BinaryTreeNode, node2: BinaryTreeNode) -> bool:
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        return (
            node1.getInfo() == node2.getInfo() and
            self.areEqualAux(node1.getLeft(), node2.getLeft()) and
            self.areEqualAux(node1.getRight(), node2.getRight())
        )

def main():

    tree = BinaryTree()
    node1 = tree.insert(4, None, None)
    node2 = tree.insert(2, None, None)
    node3 = tree.insert(6, None, None)
    node4 = tree.insert(1, None, None)
    node5 = tree.insert(3, None, None)
    node6 = tree.insert(5, None, None)
    node7 = tree.insert(7, None, None)

    print(tree.toString())  # Prints: 4 2 1 3 6 5 7
    print(tree.isEmpty())  # Prints: False
    print(tree.contains(5))  # Prints: True
    print(tree.countEvenNumbers())  # Prints: 4
    print(tree.countLeaves())  # Prints: 4
    print(tree.printPreorder())  # Prints: 4 2 1 3 6 5 7
    print(tree.printInorder())  # Prints: 1 2 3 4 5 6 7
    print(tree.printPostorder())  # Prints: 1 3 2 5 7 6 4
    print(tree.countNodes())  # Prints: 7
    print(tree.getHeight())  # Prints: 2

    another_tree = BinaryTree()
    another_node1 = another_tree.insert(4, None, None)
    another_node2 = another_tree.insert(2, None, None)
    another_node3 = another_tree.insert(6, None, None)
    another_node4 = another_tree.insert(1, None, None)
    another_node5 = another_tree.insert(3, None, None)
    another_node6 = another_tree.insert(5, None, None)
    another_node7 = another_tree.insert(7, None, None)

    print(tree.areEqual(another_tree))  # Prints: True
    
if __name__== "__main__":
    main()
