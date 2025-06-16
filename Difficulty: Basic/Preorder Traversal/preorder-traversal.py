#User function Template for python3



'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        ans=[]
        def rec(root, arr):
            if not root:
                return 
            ans.append(root.data)
            rec(root.left, arr)
            rec(root.right, arr)
        rec(root, ans)
        return ans
   
    # code here


