# Simple structure representing a binary tree node in python
class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None       # Pointer to left child
        self.right = None     # Pointer to right child
