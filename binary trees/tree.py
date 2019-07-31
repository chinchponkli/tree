# Simple structure representing a binary tree node in python
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None       # Pointer to left child
        self.right = None     # Pointer to right child
