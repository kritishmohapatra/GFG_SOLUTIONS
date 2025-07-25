class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        maxi=-sys.maxsize-1
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            if s>maxi:
                maxi=s
            if s<0:
                s=0
            
        return maxi
