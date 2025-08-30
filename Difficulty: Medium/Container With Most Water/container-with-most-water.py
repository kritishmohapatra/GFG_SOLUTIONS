class Solution:
    def maxWater(self, arr):
        # code here
        s=0
        e=len(arr)-1
        maxi=0
        a=0
        while s<e:
            a=min(arr[s],arr[e])*(e-s)
            maxi=max(maxi, a)
            if arr[s]<arr[e]:
                s+=1
            else:
                e-=1
        return maxi