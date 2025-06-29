class Solution:
    
    #Function to find minimum number of pages.
    def count(self, arr, pages):
        s=1
        ps=0
        for i in range(len(arr)):
            if ps+arr[i]<=pages:
                ps+=arr[i]
            else:
                s+=1
                ps=arr[i]
        return s
    
    def findPages(self, arr, k):
        #code here
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



