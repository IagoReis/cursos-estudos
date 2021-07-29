class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right: None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root

        self.simetric_traversal(node.left)


if __name__ == "__main__":
    tree = BinaryTree("+")
    tree.root.left = Node("18")
    tree.root.right = Node("14")

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)

    tree.simetric_traversal()