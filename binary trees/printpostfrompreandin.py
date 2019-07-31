'''
Given Inorder and Preorder traversals of a binary tree, print Postorder traversal.

Example:

Input:
Inorder traversal in[] = {4, 2, 1, 5, 3, 6}
Preorder traversal pre[] = {1, 2, 4, 3, 5, 6}

Output:
Postorder traversal is {4, 2, 5, 6, 3, 1}
'''
def printPost(pre, ino, preIndex, start, end):
    if pre[preIndex] in ino:
        root = ino.index(pre[preIndex])
    offset = root - start
    if root != start:
        printPost(pre, ino, preIndex + 1, start, root - 1)
    if root != end:
        printPost(pre, ino, preIndex + offset + 1, root + 1, end)
    print pre[preIndex],

def printPostArrayCopy(pre, ino):
    if pre[0] in ino:
        root = ino.index(pre[0])
    if root != 0:
        printPost(pre[1:root + 1], ino[:root])
    if root != len(ino) - 1:
        printPost(pre[root+1:], ino[root+1:])
    print pre[preIndex],

ino = [4, 2, 1, 5, 3, 6]
pre = [1, 2, 4, 3, 5, 6]

printPost(pre, ino, 0, 0, len(ino) - 1)
