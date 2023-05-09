#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

// Function to create a new node with a given value
TreeNode* newNode(int val) {
    TreeNode* node = new TreeNode;
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

class BinaryTree {
public:
    BinaryTree() {
        root = NULL;
    }

    bool isEmpty() {
        return root == NULL;
    }

    bool hasEven() {
        return hasEvenHelper(root);
    }

    bool hasEvenHelper(TreeNode* node) {
        if (node == NULL) {
            return false;
        }
        if (node->val % 2 == 0) {
            return true;
        }
        return hasEvenHelper(node->left) || hasEvenHelper(node->right);
    }

    int height() {
        return heightHelper(root);
    }

    int heightHelper(TreeNode* node) {
        if (node == NULL) {
            return 0;
        }
        int leftHeight = heightHelper(node->left);
        int rightHeight = heightHelper(node->right);
        return 1 + std::max(leftHeight, rightHeight);
    }

    void insert(int val) {
        if (root == NULL) {
            root = newNode(val);
        }
        else {
            insertHelper(root, val);
        }
    }

    void insertHelper(TreeNode* node, int val) {
        if (val < node->val) {
            if (node->left == NULL) {
                node->left = newNode(val);
            }
            else {
                insertHelper(node->left, val);
            }
        }
        else {
            if (node->right == NULL) {
                node->right = newNode(val);
            }
            else {
                insertHelper(node->right, val);
            }
        }
    }

    void printTree() {
        if (root == NULL) {
            std::cout << "Empty Tree" << std::endl;
        }
        else {
            printHelper(root);
        }
    }

    void printHelper(TreeNode* node) {
        if (node == NULL) {
            return;
        }
        printHelper(node->left);
        std::cout << node->val << " ";
        printHelper(node->right);
    }

private:
    TreeNode* root;
};

int main() {
    BinaryTree tree;
    tree.insert(5);
    tree.insert(3);
    tree.insert(7);
    tree.insert(1);
    tree.insert(9);

    tree.printTree();

    if (tree.isEmpty()) {
        cout << "Tree is empty" << endl;
    }
    else {
        cout << "Tree is not empty" << endl;
    }

    if (tree.hasEven()) {
        cout << "Tree has even numbers" << endl;
    }
    else {
        cout << "Tree does not have even numbers" << endl;
    }

    cout << "Tree height: " << tree.height() << endl;

    return 0;
}
