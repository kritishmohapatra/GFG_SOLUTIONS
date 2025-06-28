#User function Template for python3


class Solution:
    def solve(self,root,minval,maxval):
        if root==None:
            return True
        if root.data>=maxval or root.data<=minval:
            return False
        return self.solve(root.left,minval,root.data) and self.solve(root.right,root.data,maxval)
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        return self.solve(root,float("-inf"),float("inf"))




