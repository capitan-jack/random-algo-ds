class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, root, data):
        if data<root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
    
    def level_order_traversal(self):
        if self.root == None:
            return
        dum_que = []
        dum_que.append(self.root)
        dum_que.append('a')
        while len(dum_que) > 0:
            deque = dum_que[0]
            dum_que = dum_que[1:len(dum_que)]
            if deque == 'a':
                print()
                if len(dum_que)>0:
                    dum_que.append('a')
            else:
                if deque.left != None:
                    dum_que.append(deque.left)
                if deque.right != None:
                    dum_que.append(deque.right)
                print(deque.data)
    
    def level_order_zigzag(self):
        if self.root == None:
            return
        dum_que = []
        levels = {1:[]}
        curr_level = 1
        dum_que.append(self.root)
        dum_que.append('a')
        while len(dum_que) > 0:
            deque = dum_que[0]
            dum_que = dum_que[1:len(dum_que)]
            if deque == 'a':
                if len(dum_que)>0:
                    curr_level += 1
                    levels[curr_level] = []
                    dum_que.append('a')
            else:
                levels[curr_level].append(deque.data)
                if deque.left != None:
                    dum_que.append(deque.left)
                if deque.right != None:
                    dum_que.append(deque.right)
        for level, nodes in levels.items():
            if level%2 == 0:
                print(*nodes)
            else:
                print(*list(reversed(nodes)))

bst = BST()
bst.insert(20)
bst.insert(12)
bst.insert(32)
bst.insert(4)
bst.insert(9)
bst.insert(17)
bst.insert(14)
bst.insert(24)
bst.insert(41)
bst.insert(1)

bst.level_order_traversal()
bst.level_order_zigzag()
