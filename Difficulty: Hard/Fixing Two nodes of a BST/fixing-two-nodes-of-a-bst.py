'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __init__(self):
        self.fst=None
        self.lst=None
        self.mid=None
        self.prev=None
    def ino(self, root):
        if root is None:
            return 
        self.ino(root.left)
        if self.prev is not None and root.data<self.prev.data:
            if self.fst is None:
                self.fst=self.prev
                self.mid=root
            else:
                self.lst=root
        self.prev=root
        self.ino(root.right)
    def correctBST(self, root):
    # your code here
        self.fst=self.lst=self.mid=None
        self.prev=Node(float("-inf"))
        self.ino(root)
        if self.fst and self.lst:
            self.lst.data, self.fst.data=self.fst.data,self.lst.data
        elif self.fst and self.mid:
            self.mid.data ,self.fst.data=self.fst.data,self.mid.data