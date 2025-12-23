class Solution:
    def countLessEqual(self, arr, x):
        #code here
        lth=len(arr)
        piv=0
        for idx in range(lth-1):
            if arr[idx]>arr[idx+1]:
                piv=idx+1
                break
        import bisect
        ret=bisect.bisect_right(arr,x,0,piv)
        return ret+bisect.bisect_right(arr,x,piv,lth)-piv

