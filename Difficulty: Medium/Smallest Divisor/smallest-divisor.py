import math
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        def calci(arr, value):
            total=0
            for i in arr:
                total+=math.ceil(i/value)
            return total 
        low=1
        high=max(arr)
        res=max(arr)
        while(low<=high):
            mid=(low+high)//2
            total=calci(arr, mid)
            if total<=k:
                res=min(res, mid)
                high=mid-1
            else:
                low=mid+1
        return res
            