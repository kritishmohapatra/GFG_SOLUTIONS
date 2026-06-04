class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        sl=-1
        l=arr[0]
        for i in range(1, len(arr)):
            if arr[i]>l:
                sl=l
                l=arr[i]
            elif arr[i]<l and arr[i]>sl:
                sl=arr[i]
        return sl