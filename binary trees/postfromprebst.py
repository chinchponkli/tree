'''
Given an array representing preorder traversal of BST, print its postorder traversal.

Examples:

Input : 40 30 35 80 100
Output : 35 30 100 80 40

Input : 40 30 32 35 80 90 100 120
Output : 35 32 30 120 100 90 80 40

Time Complexity: O(n)
'''
INT_MIN = -2**31
INT_MAX = 2**31

def findPostOrderUtil(pre, n, minval, maxval, preIndex):
    # if entire array is traversed do nothing
    if (preIndex[0] == n):
        return

    # If array element does not lie in
    # range specified, then it is not
    # part of current subtree.
    if (pre[preIndex[0]] < minval or pre[preIndex[0] ] > maxval):
        return

    # Store current value, to be printed later,
    # after printing left and right subtrees.
    # Increment preIndex to find left and right
    # subtrees, and pass this updated value to
    # recursive calls.
    val = pre[preIndex[0]]
    preIndex[0] += 1

    # All elements with value between minval
    # and val lie in left subtree.
    findPostOrderUtil(pre, n, minval, val, preIndex)

    # All elements with value between val
    # and maxval lie in right subtree.
    findPostOrderUtil(pre, n, val, maxval, preIndex)

    print val,

# Function to find postorder traversal.
def findPostOrder(pre):
    preIndex = [0]
    findPostOrderUtil(pre, len(pre), INT_MIN, INT_MAX, preIndex)

pre = [40, 30, 32, 35, 80, 90, 100, 120]
findPostOrder(pre)
