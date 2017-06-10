from Node_05 import Node
from Node_05 import leafNode

class RBT:
    def __init__(self):
        self.root = None
        self.iNode = 0
        self.dNode = 0
        self.mNode = 0

    def search(self, tree, val):
        if self.root is None:
            print("The tree doesn' have any node.")
            return None
            self.mNode += 1
            
        if tree.val is None:
            print("The node", val, " is not in the tree.")
            return None
            self.mNode += 1
            
        if tree.val > val:
            return self.search(tree.left, val)
        elif tree.val < val:
            return self.search(tree.right, val)
        else:
            return tree
    
    def minimum(self, tree): #leftmost node in the tree is the minimum 
        if tree.left.val is None:
            return tree
        else:
            return self.minimum(tree.left)

    def transplant(self, tree, newtree):
        if tree.parent is None:
            self.root = newtree
        elif tree == tree.parent.left:
            tree.parent.left = newtree
        else:
            tree.parent.right = newtree
        if newtree is not None:
            newtree.parent = tree.parent

    def insert(self, n):
        # inititate 
        tree = self.root
        new = Node(n)
        y = None
        x = self.root
        self.iNode += 1

        # search a place for insertion
        while x is not None and x.val is not None:
            y = x
            if new.val < x.val:
                x = x.left
            else:
                x = x.right

        # insert new node to the place found above 
        new.parent = y
        if y is None:
            self.root = new
        elif new.val < y.val:
            y.left = new
        else:
            y.right = new

        # fix up RBT
        self.RBT_Insert_Fixup(self, new)

    def RBT_Insert_Fixup(self, tree, n):
        #property 4 is violated 
        while n.parent is not None and n.parent.parent is not None and n.parent.color is 'RED':
            #part 1  
            if n.parent == n.parent.parent.left:
                y = n.parent.parent.right
                #case1
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.right:
                        #case 2
                        n = n.parent
                        self.Left_Rotate(tree, n)
                    #case 3 
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Right_Rotate(tree, n.parent.parent)
            #part 2 
            else:
                y = n.parent.parent.left
                # case1
                if y is not None and y.color == "RED":
                    n.parent.color = "BLACK"
                    y.color = "BLACK"
                    n.parent.parent.color = "RED"
                    n = n.parent.parent
                else:
                    if n == n.parent.left:
                        #case 2 
                        n = n.parent
                        self.Right_Rotate(tree, n)
                    #case 3
                    n.parent.color = "BLACK"
                    n.parent.parent.color = "RED"
                    self.Left_Rotate(tree, n.parent.parent)
        self.root.color = "BLACK"

    def delete(self, n):
        tree = self.root
        self.dNode += 1 
        
        delNode = self.search(tree, n)
        
        if delNode is None:
            return

        y = delNode
        yOrgColor = y.color

        #case 1:delNode has no left child
        if delNode.left.val == None: 
            x = delNode.right
            self.transplant(delNode, delNode.right)

        #case 2:delNode has one left child             
        elif delNode.right.val == None:
            x = delNode.left
            self.transplant(delNode, delNode.left)

        #case 3&4: delNode has both childeren
        #then make use of successor by implementng minimum function
        else:
            y = self.minimum(delNode.right)
            yOrgColor = y.color
            x = y.right

            if y.parent is delNode:
                x.parent = delNode.right
            else:
                # y's right is delNodee's right
                self.transplant(y, y.right)
                y.right = delNode.right
                y.right.parent = y
            # Transplant y to delNode
            self.transplant(delNode, y)
            # y's left is delNode's left
            y.left = delNode.left
            y.left.parent = y
            y.color = delNode.color # y's color is delNode's original color
        
        if yOrgColor == "BLACK":
            self.RBT_Delete_Fixup(self, x)

    def RBT_Delete_Fixup(self, tree, x):
        
        while x is not tree.root and x.color == "BLACK":
            # x is located at the left side
            if x == x.parent.left:

                # w is x's sibling
                w = x.parent.right

                # Case 1
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.Left_Rotate(tree, x.parent)
                    # Change w to x's sibling
                    w = x.parent.right

                # Case 2
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent

                # Case 3
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.Right_Rotate(tree, w)
                        w = x.parent.right

                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.Left_Rotate(tree, x.parent)
                    x = tree.root

            # x is located at the right side
            else:

                # w is x's sibling
                w = x.parent.left

                # Case 1
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.Right_Rotate(tree, x.parent)
                    # Change w to x's sibling
                    w = x.parent.left

                # Case 2
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent

                # Case 3
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.Left_Rotate(tree, w)
                        w = x.parent.left

                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.Right_Rotate(tree, x.parent)
                    x = tree.root
        if x is not None:
            x.color = "BLACK"

    def Left_Rotate(self, tree, x):
        #initiate y 
        y = x.right

        # turn y's left subtree into x's right subtree
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        # link x's parent to y
        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # put x on y's left
        y.left = x
        x.parent = y

    def Right_Rotate(self, tree, x):
        # initiate y
        y = x.left

        # turn y's right subtree into x's left subtree 
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        # link x's parent to y
        y.parent = x.parent
        if x.parent is None:
            tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # put x on y's right
        y.right = x
        x.parent = y

    def print(self, tree, level):
        if tree.right.val is not None:
            self.print(tree.right, level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val, tree.color)
        if tree.left.val is not None:
            self.print(tree.left, level + 1)

    def totalNode(self, tree, n = 0):
        if tree.val is None:
            return 0
        else:
            return self.totalNode(tree.left) + self.totalNode(tree.right) + 1

    def printTotalNode(self, tree):
        print('total = ', self.totalNode(tree))

    def blackNode(self, tree):
        if tree.val is None:
            return 0
        elif tree.color == "BLACK":
            return self.blackNode(tree.left) + self.blackNode(tree.right) + 1
        else:
            return self.blackNode(tree.left) + self.blackNode(tree.right)

    def printBlackNode(self, tree):
        print('nb = ', self.blackNode(tree))

    def blackHeight(self, tree, n = 0):
        if tree.val is None:
            return 0
        elif tree.color == "BLACK":
            return self.blackHeight(tree.left) + 1
        else:
            return self.blackHeight(tree.left)

    def printBlackHeight(self, tree, n = 0):
        print('bh = ', self.blackHeight(tree, n))

    def inOrderTraversal(self, tree):
        if tree.left.val is not None:
            self.inOrderTraversal(tree.left)
        print(tree.val, tree.color)
        if tree.right.val is not None:
            self.inOrderTraversal(tree.right)

    def printInsertedNode(self, tree):
        print("insert = ", self.iNode)

    def printDeletedNode(self, tree):
        print("deleted = ", self.dNode)

    def printMissedNode(self, tree):
        print("miss = ", self.mNode)
