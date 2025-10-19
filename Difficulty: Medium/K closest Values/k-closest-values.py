'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import heapq
class Solution:
    def getKClosest(self, root, target, k):
        # code here
        queue = []
        
        heapq.heapify(queue)
        
        def dfs(root):
            nonlocal queue
            if not root:
                return
            
            heapq.heappush(queue,[abs(target-root.data),root.data])
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        res = []
        
        for i in range(k):
            _, val = heapq.heappop(queue)
            res.append(val)
            
        return res
        
    