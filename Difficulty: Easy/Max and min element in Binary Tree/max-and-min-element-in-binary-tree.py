'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def findMax(self,root):
        #code here
        if root is None:
            return float('-inf')
        res = root.data
        lres = self.findMax(root.left)
        rres = self.findMax(root.right)
        return max(res, lres, rres)
    def findMin(self,root):
        #code here
        if root is None:
            return float('inf')
        res = root.data
        lres = self.findMin(root.left)
        rres = self.findMin(root.right)
        return min(res, lres, rres)