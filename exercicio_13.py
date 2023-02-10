''' Crie uma árvore para cada lista abaixo, adicione um valor nela e remova outro, mas, em pelo menos uma das árvores, a remoção deve ser de um nó com dois filhos.
Lista1 = 45,20,30,60,81,97,100,7,8,4
Lista2 = 15,6,18,3,7,16,20,4 '''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def remove(self, value):
        if self.root is None:
            return
        else:
            parent = None
            current = self.root
            while current is not None and current.value != value:
                parent = current
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            if current is None:
                return
            elif current.left is None and current.right is None:
                if parent is None:
                    self.root = None
                elif parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            elif current.left is None or current.right is None:
                if current.left is not None:
                    nxt = current.left
                else:
                    nxt = current.right
                if parent is None:
                    self.root = nxt
                elif parent.left == current:
                    parent.left = nxt
                else:
                    parent.right = nxt
            else:
                parent = current
                nxt = current.right
                while nxt.left is not None:
                    parent = nxt
                    nxt = nxt.left
                current.value = nxt.value
                if parent.left == nxt:
                    parent.left = nxt.right
                else:
                    parent.right = nxt.right

bst = BinarySearchTree()
lista1 = [45, 20, 30, 60, 81, 97, 100, 7, 8, 4]
lista2 = [15, 6, 18, 3, 7, 16, 20, 4]

for item in lista1:
    bst.insert(item)

bst.remove(30) # removing a node with no children
bst.remove(81) # removing a node with two children

for item in lista2:
    bst.insert(item)

bst.remove(15) # removing a node with one child
