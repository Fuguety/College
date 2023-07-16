#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

class BinaryTreeNode {
private:
    int info;
    BinaryTreeNode* left;
    BinaryTreeNode* right;

public:
    BinaryTreeNode(int info, BinaryTreeNode* left = nullptr, BinaryTreeNode* right = nullptr)
        : info(info), left(left), right(right) {}

    void setInfo(int info) {
        this->info = info;
    }

    int getInfo() const {
        return info;
    }

    void setLeft(BinaryTreeNode* left) {
        this->left = left;
    }

    BinaryTreeNode* getLeft() const {
        return left;
    }

    void setRight(BinaryTreeNode* right) {
        this->right = right;
    }

    BinaryTreeNode* getRight() const {
        return right;
    }

    string toString() const {
        return to_string(info);
    }
};

class BinaryTree {
private:
    BinaryTreeNode* root;

public:
    BinaryTree() : root(nullptr) {}

    BinaryTreeNode* insert(int value, BinaryTreeNode* left, BinaryTreeNode* right) {
        BinaryTreeNode* new_node = new BinaryTreeNode(value, left, right);
        if (root == nullptr) {
            root = new_node;
        } else {
            insertNode(root, new_node);
        }
        return new_node;
    }

    void insertNode(BinaryTreeNode* current_node, BinaryTreeNode* new_node) {
        if (new_node->getInfo() < current_node->getInfo()) {
            if (current_node->getLeft() == nullptr) {
                current_node->setLeft(new_node);
            } else {
                insertNode(current_node->getLeft(), new_node);
            }
        } else {
            if (current_node->getRight() == nullptr) {
                current_node->setRight(new_node);
            } else {
                insertNode(current_node->getRight(), new_node);
            }
        }
    }

    bool isEmpty() const {
        return root == nullptr;
    }

    string toString() const {
        return toStringAux(root);
    }

    string toStringAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return "";
        } else {
            string result = toStringAux(node->getLeft());
            result += node->toString() + " ";
            result += toStringAux(node->getRight());
            return result;
        }
    }

    bool contains(int info) const {
        return containsNode(root, info);
    }

    bool containsNode(BinaryTreeNode* node, int info) const {
        if (node == nullptr) {
            return false;
        } else if (info == node->getInfo()) {
            return true;
        } else if (info < node->getInfo()) {
            return containsNode(node->getLeft(), info);
        } else {
            return containsNode(node->getRight(), info);
        }
    }

    int countEvenNumbers() const {
        return countEvenNumbersNode(root);
    }

    int countEvenNumbersNode(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return 0;
        }
        int count = 0;
        if (node->getInfo() % 2 == 0) {
            count += 1;
        }
        count += countEvenNumbersNode(node->getLeft());
        count += countEvenNumbersNode(node->getRight());
        return count;
    }

    int countLeaves() const {
        return countLeavesNode(root);
    }

    int countLeavesNode(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return 0;
        } else if (node->getLeft() == nullptr && node->getRight() == nullptr) {
            return 1;
        } else {
            return countLeavesNode(node->getLeft()) + countLeavesNode(node->getRight());
        }
    }

    string printPreorder() const {
        return printPreorderAux(root);
    }

    string printPreorderAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return "";
        }
        string result = node->toString() + " ";
        result += printPreorderAux(node->getLeft());
        result += printPreorderAux(node->getRight());
        return result;
    }

    string printInorder() const {
        return printInorderAux(root);
    }

    string printInorderAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return "";
        }
        string result = printInorderAux(node->getLeft());
        result += node->toString() + " ";
        result += printInorderAux(node->getRight());
        return result;
    }

    string printPostorder() const {
        return printPostorderAux(root);
    }

    string printPostorderAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return "";
        }
        string result = printPostorderAux(node->getLeft());
        result += printPostorderAux(node->getRight());
        result += node->toString() + " ";
        return result;
    }

    int countNodes() const {
        return countNodesAux(root);
    }

    int countNodesAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return 0;
        }
        return 1 + countNodesAux(node->getLeft()) + countNodesAux(node->getRight());
    }

    int getHeight() const {
        return getHeightAux(root);
    }

    int getHeightAux(BinaryTreeNode* node) const {
        if (node == nullptr) {
            return -1;
        }
        int left_height = getHeightAux(node->getLeft());
        int right_height = getHeightAux(node->getRight());
        return 1 + max(left_height, right_height);
    }

    bool areEqual(const BinaryTree& tree) const {
        return areEqualAux(root, tree.root);
    }

    bool areEqualAux(BinaryTreeNode* node1, BinaryTreeNode* node2) const {
        if (node1 == nullptr && node2 == nullptr) {
            return true;
        } else if (node1 == nullptr || node2 == nullptr) {
            return false;
        }
        return node1->getInfo() == node2->getInfo() &&
               areEqualAux(node1->getLeft(), node2->getLeft()) &&
               areEqualAux(node1->getRight(), node2->getRight());
    }
};

int main() {
    BinaryTree tree;
    BinaryTreeNode* node1 = tree.insert(4, nullptr, nullptr);
    BinaryTreeNode* node2 = tree.insert(2, nullptr, nullptr);
    BinaryTreeNode* node3 = tree.insert(6, nullptr, nullptr);
    BinaryTreeNode* node4 = tree.insert(1, nullptr, nullptr);
    BinaryTreeNode* node5 = tree.insert(3, nullptr, nullptr);
    BinaryTreeNode* node6 = tree.insert(5, nullptr, nullptr);
    BinaryTreeNode* node7 = tree.insert(7, nullptr, nullptr);

    cout << tree.toString() << endl;          // Prints: 4 2 1 3 6 5 7
    cout << tree.isEmpty() << endl;           // Prints: 0 (false)
    cout << tree.contains(5) << endl;         // Prints: 1 (true)
    cout << tree.countEvenNumbers() << endl;  // Prints: 4
    cout << tree.countLeaves() << endl;       // Prints: 4
    cout << tree.printPreorder() << endl;     // Prints: 4 2 1 3 6 5 7
    cout << tree.printInorder() << endl;      // Prints: 1 2 3 4 5 6 7
    cout << tree.printPostorder() << endl;    // Prints: 1 3 2 5 7 6 4
    cout << tree.countNodes() << endl;        // Prints: 7
    cout << tree.getHeight() << endl;         // Prints: 2

    BinaryTree another_tree;
    BinaryTreeNode* another_node1 = another_tree.insert(4, nullptr, nullptr);
    BinaryTreeNode* another_node2 = another_tree.insert(2, nullptr, nullptr);
    BinaryTreeNode* another_node3 = another_tree.insert(6, nullptr, nullptr);
    BinaryTreeNode* another_node4 = another_tree.insert(1, nullptr, nullptr);
    BinaryTreeNode* another_node5 = another_tree.insert(3, nullptr, nullptr);
    BinaryTreeNode* another_node6 = another_tree.insert(5, nullptr, nullptr);
    BinaryTreeNode* another_node7 = another_tree.insert(7, nullptr, nullptr);

    cout << tree.areEqual(another_tree) << endl;  // Prints: 1 (true)

    return 0;
}
