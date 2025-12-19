class Solution:
    def searchInsertK(self, arr, k):
        # code here
        N=len(arr)
        low=0
        high=N-1
        ans=N
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans