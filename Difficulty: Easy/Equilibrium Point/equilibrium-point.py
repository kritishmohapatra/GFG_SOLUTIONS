class Solution:
    def findEquilibrium(self, arr):
        # code here
        t=sum(arr)
        l=0
        for i in range(len(arr)):
            r=t-arr[i]-l
            if r==l:
                return i
            l+=arr[i]
        return -1

