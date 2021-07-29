class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
            if self.root is None:
                return
            node = self.root

        if node.left:
            self.simetric_traversal(node.left)

        print(node, end=", ")

        if node.right:
            self.simetric_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node and node.left:
            self.postorder_traversal(node.left)

        if node and node.right:
            self.postorder_traversal(node.right)

        if node and node.data:
            print(node, end=', ')

    def height(self, node=None):

        if node is None:
            node = self.root

        left_size = 0
        right_size = 0

        if node.left:
            left_size = self.height(node.left)

        if node.right:
            right_size = self.height(node.right)

        if left_size > right_size:
            return left_size + 1
        else:
            return right_size + 1


class BinarySearchTree(BinaryTree):
    def __init__(self, node=None):
        if node:
            self.root = node
        else:
            self.root = None

    def add(self, value):
        parent = None
        leaf = self.root
        while leaf:
            parent = leaf
            if value < leaf.data:
                leaf = leaf.left
            else:
                leaf = leaf.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):

        if node == 0:
            node = self.root
        if node is None or value == node.data:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)


if __name__ == "__main__":
    tree = BinaryTree()
    n3 = Node("1")
    n4 = Node("2")

    n1 = Node("+")
    n1.left = n3
    n1.right = n4

    n2 = Node("+")
    n2.left = Node("3")
    n2.right = Node("4")

    root = Node("*")
    root.left = n1
    root.right = n2

    tree = BinaryTree()
    tree.root = root

    tree.simetric_traversal()

    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9

    n6.left = n1
    n6.right = n5

    n5.left = n2
    n5.right = n4

    n4.right = n3

    n9.left = n8
    n9.right = Node('-')

    n8.right = n7

    potree = BinaryTree()
    potree.root = n0

    potree.postorder_traversal()
    print()

    print("Tamanho da árvore: {}".format(potree.height()))

    print()
    print("##### Árvore Binária de Busca #####")
    print()

    bst = BinarySearchTree()
    bst.add(10)
    bst.add(11)
    bst.add(20)
    bst.add(5)
    bst.add(7)
    bst.add(89)
    bst.add(100)
    bst.add(165)
    bst.add(33)
    bst.add(45)

    print("IN ORDER")
    bst.simetric_traversal()

    print()
    print()
    print()
    valor = 89
    print("Procurando {}".format(valor))
    st = bst.search(valor)
    if st.root is None:
        print("{} não foi encontrado".format(valor))
    print()
    print("IN ORDER")
    st.simetric_traversal()
    print()
    print("POST ORDER")
    st.postorder_traversal()
