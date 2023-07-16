#include <iostream>
#include <string>

using namespace std;

class BinaryTreeNode {
private:
    int info;
    BinaryTreeNode* left;
    BinaryTreeNode* right;

public:
    BinaryTreeNode(int info, BinaryTreeNode* left = nullptr, BinaryTreeNode* right = nullptr) {
        this->info = info;
        this->left = left;
        this->right = right;
    }

    void setInfo(int info) {
        this->info = info;
    }

    int getInfo() {
        return this->info;
    }

    void setLeft(BinaryTreeNode* left) {
        this->left = left;
    }

    BinaryTreeNode* getLeft() {
        return this->left;
    }

    void setRight(BinaryTreeNode* right) {
        this->right = right;
    }

    BinaryTreeNode* getRight() {
        return this->right;
    }

    string toString() {
        return to_string(this->info);
    }
};

class BinarySearchTree {
private:
    BinaryTreeNode* root;

public:
    BinarySearchTree() {
        this->root = nullptr;
    }

    BinaryTreeNode* search(int v) {
        return searchRecursive(this->root, v);
    }

    BinaryTreeNode* searchRecursive(BinaryTreeNode* node, int v) {
        if (node == nullptr || v == node->getInfo()) {
            return node;
        }

        if (v < node->getInfo()) {
            return searchRecursive(node->getLeft(), v);
        } else {
            return searchRecursive(node->getRight(), v);
        }
    }

    void insert(int v) {
        this->root = insertRecursive(this->root, v);
    }

    BinaryTreeNode* insertRecursive(BinaryTreeNode* node, int v) {
        if (node == nullptr) {
            return new BinaryTreeNode(v);
        }

        if (v < node->getInfo()) {
            node->setLeft(insertRecursive(node->getLeft(), v));
        } else {
            node->setRight(insertRecursive(node->getRight(), v));
        }

        return node;
    }

    void remove(int v) {
        this->root = removeRecursive(this->root, v);
    }

    BinaryTreeNode* removeRecursive(BinaryTreeNode* node, int v) {
        if (node == nullptr) {
            return node;
        }

        if (v < node->getInfo()) {
            node->setLeft(removeRecursive(node->getLeft(), v));
        } else if (v > node->getInfo()) {
            node->setRight(removeRecursive(node->getRight(), v));
        } else {
            if (node->getLeft() == nullptr) {
                return node->getRight();
            } else if (node->getRight() == nullptr) {
                return node->getLeft();
            }

            BinaryTreeNode* temp = minimum(node->getRight());
            node->setInfo(temp->getInfo());
            node->setRight(removeRecursive(node->getRight(), temp->getInfo()));
        }

        return node;
    }

    BinaryTreeNode* minimum(BinaryTreeNode* node) {
        while (node->getLeft() != nullptr) {
            node = node->getLeft();
        }
        return node;
    }

    string toString() {
        return inOrder(this->root);
    }

    string inOrder(BinaryTreeNode* node) {
        if (node == nullptr) {
            return "";
        }

        string result = inOrder(node->getLeft());
        result += to_string(node->getInfo()) + " ";
        result += inOrder(node->getRight());

        return result;
    }

    string toStringDescending() {
        return inOrderDescending(this->root);
    }

    string inOrderDescending(BinaryTreeNode* node) {
        if (node == nullptr) {
            return "";
        }

        string result = inOrderDescending(node->getRight());
        result += to_string(node->getInfo()) + " ";
        result += inOrderDescending(node->getLeft());

        return result;
    }

    int sumLeaves() {
        return sumLeavesRecursive(this->root);
    }

    int sumLeavesRecursive(BinaryTreeNode* node) {
        if (node == nullptr) {
            return 0;
        }

        if (node->getLeft() == nullptr && node->getRight() == nullptr) {
            return node->getInfo();
        }

        return sumLeavesRecursive(node->getLeft()) + sumLeavesRecursive(node->getRight());
    }

    int greaterThanX(int x) {
        return greaterThanXRecursive(this->root, x);
    }

    int greaterThanXRecursive(BinaryTreeNode* node, int x) {
        if (node == nullptr) {
            return 0;
        }

        if (node->getInfo() > x) {
            return 1 + greaterThanXRecursive(node->getLeft(), x) + greaterThanXRecursive(node->getRight(), x);
        } else {
            return greaterThanXRecursive(node->getRight(), x);
        }
    }
};

int main() {
    BinarySearchTree tree;

    tree.insert(8);
    tree.insert(3);
    tree.insert(10);
    tree.insert(1);
    tree.insert(6);
    tree.insert(14);
    tree.insert(4);
    tree.insert(7);
    tree.insert(13);

    cout << "Tree in ascending order:" << endl;
    cout << tree.toString() << endl;

    cout << "\nTree in descending order:" << endl;
    cout << tree.toStringDescending() << endl;

    int search_value = 6;
    BinaryTreeNode* node = tree.search(search_value);
    if (node != nullptr) {
        cout << "\nElement " << search_value << " found in the tree." << endl;
    } else {
        cout << "\nElement " << search_value << " not found in the tree." << endl;
    }

    int remove_value = 4;
    tree.remove(remove_value);
    cout << "\nTree after removing element " << remove_value << ":" << endl;
    cout << tree.toString() << endl;

    int sum_leaves = tree.sumLeaves();
    cout << "\nSum of leaf node values in the tree: " << sum_leaves << endl;

    int x = 7;
    int greater_than_x = tree.greaterThanX(x);
    cout << "\nNumber of elements greater than " << x << " in the tree: " << greater_than_x << endl;

    return 0;
}
