class Solution:
    def maxCircularSum(self, arr):
        # code here
        minsum=float("inf")
        maxsum=float("-inf")
        t=0
        s1, s2=0, 0
        for i in range(0, len(arr)):
            t+=arr[i]
            s1=max(s1+arr[i], arr[i])
            maxsum=max(s1, maxsum)
            s2=min(s2+arr[i], arr[i])
            minsum=min(s2, minsum)
        if t==minsum:
            return maxsum
    
        return max(maxsum, t-minsum)
        