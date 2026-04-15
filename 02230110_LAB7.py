class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        print("Created new Binary Tree")
        print("Root:", self.root)

    def set_root(self, node):
        self.root = node

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
        if node.left and node.right:
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


bt = BinaryTree()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

bt.set_root(n1)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print("Tree Height:", bt.height(bt.root))
print("Total Nodes:", bt.size(bt.root))
print("Leaf Nodes Count:", bt.count_leaves(bt.root))
print("Is Full Binary Tree:", bt.is_full_binary_tree(bt.root))
print("Is Complete Binary Tree:", bt.is_complete_binary_tree())