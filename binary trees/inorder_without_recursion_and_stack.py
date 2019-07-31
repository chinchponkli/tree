from tree import Tree
'''
Using Morris Traversal, we can traverse the tree without using stack and
recursion. The idea of Morris Traversal is based on Threaded Binary Tree.
In this traversal, we first create links to Inorder successor and print the
data using these links, and finally revert the changes to restore original tree.

1. Initialize current as root
2. While current is not NULL
   If the current does not have left child
      a) Print current's data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as the right child of the rightmost
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left

Time Complexity: O(n)
Space Complexity: O(1).
'''

from tree import Tree

def inorder(root):
    current = root
    while current:
        if current.left is None:
            print current.data,
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right
            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print current.data,
                current = current.right

a = Tree(1)
a.left = Tree(2)
a.right = Tree(3)
a.left.left = Tree(4)
a.right.left = Tree(5)
a.right.right = Tree(6)

inorder(a)
