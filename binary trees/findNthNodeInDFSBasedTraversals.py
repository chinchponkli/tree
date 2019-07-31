'''
Write functions to find nth node for preorder, inorder and postorder traversal
of a tree.

        1
      /   \
    2       3
  /       /   \
4       5       6

For the tree above and k = 3:

ntn node in Preorder traversal is: 3
nth node in Inorder traversal is: 1
nth node in Postorder traversal is: 5
'''

from tree import Tree

def preorder(root, n, count):
    if root:
        count[0] += 1
        if n == count[0]:
            print root.data
            return
        preorder(root.left, n, count)
        preorder(root.right, n, count)

def inorder(root, n, count):
    if root:
        inorder(root.left, n, count)
        count[0] += 1
        if n == count[0]:
            print root.data
            return
        inorder(root.right, n, count)

def postorder(root, n, count):
    if root:
        postorder(root.left, n, count)
        postorder(root.right, n, count)
        count[0] += 1
        if n == count[0]:
            print root.data
            return

a = Tree(1)
a.left = Tree(2)
a.right = Tree(3)
a.left.left = Tree(4)
a.right.left = Tree(5)
a.right.right = Tree(6)

preorder(a, 3, [0])
inorder(a, 3, [0])
postorder(a, 3, [0])
