class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self, root = None):
        self.root = None
        if root != None:
            self.root = Node(root)
    
    def _traverse_in_order(self, root):
        if root != None:
            self._traverse_in_order(root.left)
            print(root.data)
            self._traverse_in_order(root.right)
    
    def traverse_in_order(self):
        self._traverse_in_order(self.root)
        
    def _random_tree(self, root, value):
        if root == None:
            return
        from random import randint
        val = randint(0,1)
        if val == 0:
            if root.left == None:
                root.left = Node(value)
                return
            self._random_tree(root.left, value)
        else:
            if root.right == None:
                root.right = Node(value)
                return
            self._random_tree(root.right, value)

    def insert(self, value):
        self._random_tree(self.root, value)

    def _find_LCA(self, root, value1, value2):
        if root == None:
            return False
        if root.data == value1:
            return True
        if root.data == value2:
            return True
        if self._find_LCA(root.left, value1, value2) and\
        self._find_LCA(root.right, value1, value2):
            return root
        return False
    
    def find_LCA(self, value1, value2):
        if self.root == None:
            return None
        if self.root.data == value1:
            return None
        if self.root.data == value2:
            return None
        ret_val = self._find_LCA(self.root, value1, value2)
        if ret_val != False:
            return ret_val.data

        
        
tree = Tree(12)
tree.random_tree(21)
tree.random_tree(17)
tree.random_tree(23)
tree.random_tree(13)
tree.random_tree(1)
tree.traverse_in_order()
print(tree.find_LCA(1, 21))
