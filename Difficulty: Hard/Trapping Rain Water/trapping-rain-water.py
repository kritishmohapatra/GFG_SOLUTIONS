
class Solution:
    def maxWater(self, arr):
        # code here
        t=0
        i=0
        j=len(arr)-1
        lm=0
        rm=0
        while i<j:
            lm=max(lm,arr[i])
            rm=max(rm, arr[j])
            if arr[i]<=arr[j]:
                t+=lm-arr[i]
                i+=1
            else:
                t+=rm-arr[j]
                j-=1
        return t