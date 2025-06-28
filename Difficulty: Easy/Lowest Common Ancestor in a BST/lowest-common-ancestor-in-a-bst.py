'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def LCA(self, root, n1, n2):
        if not root:
            return None
        while True:
            if root.data>n1.data and root.data>n2.data:
                root=root.left
            elif root.data<n1.data and root.data<n2.data:
                root=root.right
            else:
                return root
        
        
    



