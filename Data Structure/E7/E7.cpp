#include <iostream>
#include <string>

class TreeNode {
private:
    int info;
    TreeNode* first_child;
    TreeNode* next_sibling;

public:
    TreeNode(int info) {
        this->info = info;
        this->first_child = nullptr;
        this->next_sibling = nullptr;
    }

    void set_info(int info) {
        this->info = info;
    }

    int get_info() {
        return this->info;
    }

    void set_first_child(TreeNode* first_child) {
        this->first_child = first_child;
    }

    TreeNode* get_first_child() {
        return this->first_child;
    }

    void set_next_sibling(TreeNode* next_sibling) {
        this->next_sibling = next_sibling;
    }

    TreeNode* get_next_sibling() {
        return this->next_sibling;
    }

    std::string to_string() {
        return std::to_string(this->info);
    }
};

class Tree {
private:
    TreeNode* root;

public:
    Tree() {
        this->root = nullptr;
    }

    TreeNode* create_node(int info) {
        return new TreeNode(info);
    }

    void insert_child(TreeNode* parent_node, TreeNode* child_node) {
        if (parent_node->get_first_child() == nullptr) {
            parent_node->set_first_child(child_node);
        } else {
            TreeNode* current = parent_node->get_first_child();
            while (current->get_next_sibling() != nullptr) {
                current = current->get_next_sibling();
            }
            current->set_next_sibling(child_node);
        }
    }

    std::string to_string() {
        if (this->root != nullptr) {
            return this->print_tree(this->root, 0);
        } else {
            return "Empty tree.";
        }
    }

    std::string print_tree(TreeNode* node, int level) {
        std::string result = std::string(2 * level, ' ') + node->to_string() + "\n";
        if (node->get_first_child() != nullptr) {
            TreeNode* current = node->get_first_child();
            while (current != nullptr) {
                result += this->print_tree(current, level + 1);
                current = current->get_next_sibling();
            }
        }
        return result;
    }

    bool contains(int info) {
        return this->contains_aux(this->root, info);
    }

    bool contains_aux(TreeNode* node, int info) {
        if (node == nullptr) {
            return false;
        }
        if (node->get_info() == info) {
            return true;
        }
        TreeNode* current = node->get_first_child();
        while (current != nullptr) {
            if (this->contains_aux(current, info)) {
                return true;
            }
            current = current->get_next_sibling();
        }
        return false;
    }

    int height() {
        return this->height_aux(this->root);
    }

    int height_aux(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        int max_height = 0;
        TreeNode* current = node->get_first_child();
        while (current != nullptr) {
            int child_height = this->height_aux(current);
            max_height = std::max(max_height, child_height);
            current = current->get_next_sibling();
        }
        return 1 + max_height;
    }

    int count_even_numbers() {
        return this->count_even_numbers_aux(this->root);
    }

    int count_even_numbers_aux(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        int count = 0;
        if (node->get_info() % 2 == 0) {
            count += 1;
        }
        TreeNode* current = node->get_first_child();
        while (current != nullptr) {
            count += this->count_even_numbers_aux(current);
            current = current->get_next_sibling();
        }
        return count;
    }

    int count_leaf_nodes() {
        return this->count_leaf_nodes_aux(this->root);
    }

    int count_leaf_nodes_aux(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        if (node->get_first_child() == nullptr) {
            return 1;
        }
        int count = 0;
        TreeNode* current = node->get_first_child();
        while (current != nullptr) {
            count += this->count_leaf_nodes_aux(current);
            current = current->get_next_sibling();
        }
        return count;
    }

    bool is_equal(Tree* other_tree) {
        return this->is_equal_aux(this->root, other_tree->root);
    }

    bool is_equal_aux(TreeNode* node1, TreeNode* node2) {
        if (node1 == nullptr && node2 == nullptr) {
            return true;
        }
        if (node1 == nullptr || node2 == nullptr) {
            return false;
        }
        if (node1->get_info() != node2->get_info()) {
            return false;
        }
        TreeNode* current1 = node1->get_first_child();
        TreeNode* current2 = node2->get_first_child();
        while (current1 != nullptr && current2 != nullptr) {
            if (!this->is_equal_aux(current1, current2)) {
                return false;
            }
            current1 = current1->get_next_sibling();
            current2 = current2->get_next_sibling();
        }
        return current1 == nullptr && current2 == nullptr;
    }

    Tree* copy() {
        Tree* new_tree = new Tree();
        new_tree->root = this->copy_aux(this->root);
        return new_tree;
    }

    TreeNode* copy_aux(TreeNode* node) {
        if (node == nullptr) {
            return nullptr;
        }
        TreeNode* new_node = new TreeNode(node->get_info());
        TreeNode* current = node->get_first_child();
        while (current != nullptr) {
            TreeNode* new_child = this->copy_aux(current);
            if (new_node->get_first_child() == nullptr) {
                new_node->set_first_child(new_child);
            } else {
                TreeNode* temp = new_node->get_first_child();
                while (temp->get_next_sibling() != nullptr) {
                    temp = temp->get_next_sibling();
                }
                temp->set_next_sibling(new_child);
            }
            current = current->get_next_sibling();
        }
        return new_node;
    }
};

int main() {
    // Create an empty tree
    Tree tree;

    // Create nodes
    TreeNode* node1 = tree.create_node(1);
    TreeNode* node2 = tree.create_node(2);
    TreeNode* node3 = tree.create_node(3);
    TreeNode* node4 = tree.create_node(4);
    TreeNode* node5 = tree.create_node(5);
    TreeNode* node6 = tree.create_node(6);
    TreeNode* node7 = tree.create_node(7);
    TreeNode* node8 = tree.create_node(8);

    // Build the tree structure
    tree.insert_child(node1, node2);
    tree.insert_child(node1, node3);
    tree.insert_child(node1, node4);
    tree.insert_child(node2, node5);
    tree.insert_child(node3, node6);
    tree.insert_child(node4, node7);
    tree.insert_child(node4, node8);

    // Print the tree structure
    std::cout << tree.to_string() << std::endl;

    // Check if certain values belong to the tree
    std::cout << "Belongs to tree: " << tree.contains(3) << std::endl;
    std::cout << "Belongs to tree: " << tree.contains(9) << std::endl;

    // Calculate the height of the tree
    std::cout << "Tree height: " << tree.height() << std::endl;

    // Count the number of even numbers in the tree
    std::cout << "Number of even numbers: " << tree.count_even_numbers() << std::endl;

    // Count the number of leaf nodes in the tree
    std::cout << "Number of leaf nodes: " << tree.count_leaf_nodes() << std::endl;

    // Create a copy of the tree
    Tree* tree_copy = tree.copy();

    // Check if the copied tree is equal to the original tree
    std::cout << "Trees are equal: " << tree.is_equal(tree_copy) << std::endl;

    return 0;
}
