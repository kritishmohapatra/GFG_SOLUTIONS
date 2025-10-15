'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, low, high):
        #code here
        if not root:
            return None
        if root.data >high:
            return self.removekeys(root.left,low,high)
        if root.data<low:
            return self.removekeys(root.right,low, high)
        root.left = self.removekeys(root.left,low,high)
        root.right = self.removekeys(root.right,low, high)
        return root

