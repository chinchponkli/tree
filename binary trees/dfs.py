'''
Write functions for preorder, inorder and postorder traversal of a tree.

        1
      /   \
    2       3
  /       /   \
4       5       6

For the tree above:

Preorder traversal is: 1 2 4 3 5 6
Inorder traversal is: 4 2 1 5 3 6
Postorder traversal is: 4 2 5 6 3 1
'''

from tree import Tree

def preorder(root):
    if root:
        print root.key,
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print root.key,
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.key,

a = Tree(1)
a.left = Tree(2)
a.right = Tree(3)
a.left.left = Tree(4)
a.right.left = Tree(5)
a.right.right = Tree(6)

preorder(a)
print
inorder(a)
print
postorder(a)
