'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def updateTree(self,root, sum):
        if root is None:
            return
    
        # Traverse the right subtree first (larger values)
        self.updateTree(root.right, sum)
    
        # Update the sum and the current node's value
        sum[0] += root.data
        root.data = sum[0] - root.data
    
        # Traverse the left subtree (smaller values)
        self.updateTree(root.left, sum)
    def transformTree(self, root):
        # code here
        sum = [0]
        self.updateTree(root, sum)
        
