class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n=len(arr)
        c=0
        for i in range(k):
            c^=arr[i]
        maxi=c
        for i in range(k, n):
            c^=arr[i]
            c^=arr[i-k]
            maxi=max(c, maxi)
        return maxi
        
       