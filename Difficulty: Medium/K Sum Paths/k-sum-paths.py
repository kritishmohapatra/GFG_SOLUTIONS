'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def __init__(self):
        self.c=0
    def countAllPaths(self, root, k):
        # code here
        freq={0:1}
        def func(root,k,s,freq):
            if root==None:
                return
            s+=root.data
            if s-k in freq:
                self.c+=freq[s-k]
            freq[s]=1+freq.get(s,0)
            func(root.left,k,s,freq)
            func(root.right,k,s,freq)
            freq[s]-=1
        func(root,k,0,freq)
        return self.c