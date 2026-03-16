'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        # code here
        if root is None:
            return -1
        q=deque([root])
        tar=None
        par={root:None}
        while q:
            curr=q.popleft()
            if curr.data==target:
                tar=curr
            if curr.left:
                par[curr.left]=curr
                q.append(curr.left)
            if curr.right:
                par[curr.right]=curr
                q.append(curr.right)
        vis={}
        ans=-1
        q.append(tar)
        
        while q:
            size=len(q)
            for _ in range(size):
                curr=q.popleft()
                vis[curr]=True
                
                if curr.left and not vis.get(curr.left):
                    q.append(curr.left)
                if curr.right and not vis.get(curr.right):
                    q.append(curr.right)
                if par[curr] and not vis.get(par[curr]):
                    q.append(par[curr])
            ans+=1
        return ans
