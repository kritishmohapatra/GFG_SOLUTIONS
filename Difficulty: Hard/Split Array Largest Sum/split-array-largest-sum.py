class Solution:
    def count(self, arr, maxsum):
        n=len(arr)
        part=1
        s=0
        for i in range(n):
            if s+arr[i]<=maxsum:
                s+=arr[i]
            else:
                part+=1
                s=arr[i]
        return part
    def splitArray(self, arr, k):
        # code here
        if k>len(arr):
            return -1
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            st=self.count(arr, mid)
            if st>k:
                low=mid+1
            else:
                high=mid-1
        return low
        