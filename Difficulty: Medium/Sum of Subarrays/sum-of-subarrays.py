class Solution:
    def subarraySum(self, arr):
        # code here 
        n=len(arr)
        res=0
        for i in range(n):
            res+=arr[i]*(i+1)*(n-i)
        return res
        