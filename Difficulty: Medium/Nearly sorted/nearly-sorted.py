import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        p=[]
        j=0
        for i in range(len(arr)):
            heapq.heappush(p, arr[i])
            if len(p)>k:
                arr[j]=heapq.heappop(p)
                j+=1
        while p:
        
            arr[j]=heapq.heappop(p)
            j+=1