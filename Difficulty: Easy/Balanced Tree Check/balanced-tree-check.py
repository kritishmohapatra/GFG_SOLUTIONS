'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def dfs(self, root):
        if root==None:
            return 0
        lh=self.dfs(root.left)
        if lh==-1:
            return -1
        rh=self.dfs(root.right)
        if rh==-1:
            return -1
        if (abs(lh-rh)>1):
            return -1
        return max(lh, rh)+1
    def isBalanced(self, root):
        # code here
        return self.dfs(root)!=-1