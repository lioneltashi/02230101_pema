# -------------------------------
# Node Class
# -------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# -------------------------------
# Binary Tree Class
# -------------------------------
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return (self.is_full_binary_tree(node.left) and
                    self.is_full_binary_tree(node.right))

        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        queue = [self.root]
        flag = False

        while queue:
            current = queue.pop(0)

            if current.left:
                if flag:
                    return False
                queue.append(current.left)
            else:
                flag = True

            if current.right:
                if flag:
                    return False
                queue.append(current.right)
            else:
                flag = True

        return True

if __name__ == "__main__":

    tree = BinaryTree()

    print("Created new Binary Tree")
    print("Root:", tree.root)

    # Different structure (not perfect)
    tree.root = Node(10)
    tree.root.left = Node(20)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.right = Node(60)   # uneven structure

    print("\nTree Height:", tree.height(tree.root))
    print("Total Nodes:", tree.size(tree.root))
    print("Leaf Nodes Count:", tree.count_leaves(tree.root))
    print("Is Full Binary Tree:", tree.is_full_binary_tree(tree.root))
    print("Is Complete Binary Tree:", tree.is_complete_binary_tree())