"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        # code here
        if root is None:
            return 0
       
        if root.data < l:
            return self.nodeSum(root.right, l, r)
        
       
        elif root.data > r:
            return self.nodeSum(root.left, l, r)
    
        # If root value lies in the range.
        left = self.nodeSum(root.left, l, r)
        right = self.nodeSum(root.right, l, r)
        
        return left+right+root.data
        
