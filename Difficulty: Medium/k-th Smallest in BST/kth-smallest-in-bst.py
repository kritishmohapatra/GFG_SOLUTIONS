#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def inorder(self,root,c,k,ks):
        if not root or c[0]>=k:
            return
        self.inorder(root.left,c,k,ks)
        c[0]+=1
        if c[0]==k:
            ks[0]=root.data
            return
        self.inorder(root.right,c,k,ks)
    def kthSmallest(self, root, k): 
        #code herek
        ks=[-1]
        c=[0]
        self.inorder(root,c,k,ks)
        return ks[0]
