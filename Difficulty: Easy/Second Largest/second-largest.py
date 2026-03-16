class Solution:
    def getSecondLargest(self, a):
        # Code Here
        sl=-1
        l=a[0]
        for i in range(1, len(a)):
            if a[i]>l:
                sl=l
                l=a[i]
            elif a[i]<l and a[i]>sl:
                sl=a[i]
        return sl