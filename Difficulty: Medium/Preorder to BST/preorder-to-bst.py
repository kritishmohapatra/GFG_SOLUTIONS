#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def build(arr, i_ref, bound):
    if i_ref[0] == len(arr) or arr[i_ref[0]] > bound:
        return None

    val = arr[i_ref[0]]
    i_ref[0] += 1

    root = Node(val)
    root.left = build(arr, i_ref, val)
    root.right = build(arr, i_ref, bound)

    return root
def Bst(pre, size) -> Node:
    #code here
    i_ref = [0]  # Using list to make `i` mutable and shared across recursive calls
    return build(pre, i_ref, float('inf'))