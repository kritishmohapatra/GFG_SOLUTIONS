#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pathsum(self,root,d):
        if root is None:
            return 0
        left=max(0,self.pathsum(root.left,d))
        right=max(0,self.pathsum(root.right,d))
        d[0]=max(d[0],left+right+root.data)
        return max(left,right)+root.data
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        maxi=[float("-inf")]
        self.pathsum(root,maxi)
        return maxi[0]


