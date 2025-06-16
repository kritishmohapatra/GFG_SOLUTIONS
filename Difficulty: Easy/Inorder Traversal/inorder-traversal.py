#User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def rec(self, root, arr):
        if root is None:
            return
        self.rec(root.left, arr)
        arr.append(root.data)
        self.rec(root.right, arr)
    def inOrder(self,root):
        # code here
        ans=[]
        self.rec(root, ans)
        return ans
        
                






