class Solution:
    def replaceElements(self, arr):
        # code here
        n=len(arr)
        if n==1:
            return 
        prev=arr[0]
        arr[0]=arr[0]^arr[1]
        for i in range(1, n-1):
            curr=arr[i]
            arr[i]=prev^arr[i+1]
            prev=curr
        arr[n-1]=arr[n-1]^prev
        return arr