'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isleaf(self, root):
        return root and  not root.left and not root.right
    def addleft(self, root, res):
        curr=root.left
        while curr:
            if not self.isleaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    def addright(self, root, res):
        curr=root.right
        temp=[]
        while curr:
            if not self.isleaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])
        return res
    def addls(self, root, res):
        if not root:
            return 
        if self.isleaf(root):
            res.append(root.data)
            return 
        if root.left:
            self.addls(root.left, res)
        if root.right:
            self.addls(root.right, res)
            
                
                
        
    def boundaryTraversal(self, root):
        res=[]
        
        if not root:
            return res
        
        if not self.isleaf(root):
            res.append(root.data)
        self.addleft(root, res)
        self.addls(root, res)
        self.addright(root, res)
        return res
        # code here
        
        