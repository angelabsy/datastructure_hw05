class Node:
    def __init__(self, key):
        self.val = key
        self.left = leafNode()
        self.right = leafNode()
        self.parent = None
        self.color = 'RED'

# leaf
class leafNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = "BLACK"
