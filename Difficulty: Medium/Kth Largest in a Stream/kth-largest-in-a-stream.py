import heapq
class Solution:
    def kthLargest(self, arr, k):
        # code here 
        q=[]
        ans=[]
        for i in arr:
            heapq.heappush(q, i)
            if len(q)<k:
                ans.append(-1)
            else:
                while len(q)>k:
                    heapq.heappop(q)
                ans.append(q[0])
        return ans