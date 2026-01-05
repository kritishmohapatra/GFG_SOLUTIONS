class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        c=sum(arr[:k])
        maxi=c
        for i in range(k, len(arr)):
            c+=arr[i]-arr[i-k]
            maxi=max(maxi, c)
        return maxi