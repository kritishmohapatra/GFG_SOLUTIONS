class Solution:
    def calculateSpan(self, arr):
        # code here
        n=len(arr)
        ans=[0]*n
        s=[]
        for i in range(n):
            while s and arr[s[-1]]<=arr[i]:
                s.pop()
            if not s:
                ans[i]=i+1
            else:
                ans[i]=i-s[-1]
            s.append(i)
        return ans
        