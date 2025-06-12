from heapq import *
class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        heap=[]
        for i in arr:
            if i==x:
                continue
            else:
                heappush(heap,(abs(i-x),-i))
        res=[]
        while heap and k:
            _, val=heappop(heap)
            res.append(-val)
            k-=1
        return res