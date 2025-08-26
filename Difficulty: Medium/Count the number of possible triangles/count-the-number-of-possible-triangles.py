class Solution:
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n=len(arr)
        ans=0
        for i in range(n-1,1,-1):
            j=0
            k=i-1
            while j<k:
                if arr[j]+arr[k]>arr[i]:
                    ans+=k-j
                    k-=1
                else:
                    j+=1
        return ans
        