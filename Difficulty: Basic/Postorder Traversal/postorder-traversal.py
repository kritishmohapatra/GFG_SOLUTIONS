'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def rec(self, root, arr):
        if not root:
            return 
        self.rec(root.left, arr)
        self.rec(root.right, arr)
        arr.append(root.data)
    def postOrder(self, root):
        # code here
        arr=[]
        self.rec(root, arr)
        return arr