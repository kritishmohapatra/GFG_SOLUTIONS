class Solution:
    def kthMissing(self, arr, k):
        # code here
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            mis=arr[mid]-(mid+1)
            if mis<k:
                low=mid+1
            else:
                high=mid-1
        return high+k+1
