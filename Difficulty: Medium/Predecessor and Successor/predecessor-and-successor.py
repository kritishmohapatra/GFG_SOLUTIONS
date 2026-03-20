'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def suc(self, root, key):
        s=None
        while root!=None:
            if key>=root.data:
                root=root.right
            else:
                s=root
                root=root.left
        return s
    def pre(self, root, key):
        p=None
        while root!=None:
            if root.data>=key:
                root=root.left
            else:
                p=root
                root=root.right
        return p  
    
    def findPreSuc(self, root, key):
        # code here
        p,s=self.pre(root, key), self.suc(root, key)
        return (p,s)