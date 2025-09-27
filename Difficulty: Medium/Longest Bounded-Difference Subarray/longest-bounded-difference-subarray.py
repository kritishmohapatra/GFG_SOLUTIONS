from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        #code here
        minq=deque()
        maxq=deque()
        s,e=0,0
        l=0
        anss, anse=0,0
        for i in range(len(arr)):
            e=i
            while maxq and arr[maxq[-1]]<arr[i]:
                maxq.pop()
            maxq.append(i)
            while minq and arr[minq[-1]]>arr[i]:
                minq.pop()
            minq.append(i)
            while arr[maxq[0]]-arr[minq[0]]>x:
                s+=1
                while minq and minq[0]<s:
                    minq.popleft()
                while maxq and maxq[0]<s:
                    maxq.popleft()
            if e-s+1>l:
                l=e-s+1
                anss, anse=s,e
        return arr[anss:anse+1]
            