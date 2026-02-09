class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def calci(arr, k):
            total=0
            for i in arr:
                total+=math.ceil(i/k)
            return total
        
        low=1
        high=max(arr)
        while(low<=high):
            mid=(low+high)//2
            total=calci(arr, mid)
            if total<=k:
                high=mid-1
            else:
                low=mid+1
        return low