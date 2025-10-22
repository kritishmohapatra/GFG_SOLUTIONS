import heapq
class Solution:
    def kClosest(self, points, k):
        # code here
        
        q=[]
        ans=[]
        for x2, y2 in points:
            dis=((x2*x2)+(y2*y2))**0.5
            heapq.heappush(q, ([dis, (x2, y2)]))
        while k:
            ans.append(heapq.heappop(q)[1])
            k-=1
        return ans
        