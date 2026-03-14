'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        ans=[]
        m={}
        if not root:
            return ans
        q=deque([(root, 0)])
        while q:
            n, l=q.popleft()
            if l not in m:
                m[l]=n.data
            if n.left:
                q.append((n.left, l-1))
            if n.right:
                q.append((n.right, l+1))
        for value in sorted(m.items()):
            ans.append(value[1])
        return ans
        
        
        