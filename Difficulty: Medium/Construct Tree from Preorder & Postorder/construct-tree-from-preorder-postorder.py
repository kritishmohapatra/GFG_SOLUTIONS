'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        # code here
        def construct(pre, post):
            if not pre and not post:
                return None
            n = Node(pre[0])
            r1 = pre[1:]
            r2 = post[:len(post)-1]
            if not r1:
                return n
            i1 = r1.index(r2[-1])
            i2 = r2.index(r1[0])
            n.left = construct(r1[:i1], r2[:i2+1])
            n.right = construct(r1[i1:], r2[i2+1:])
            return n
        
        return construct(pre, post)