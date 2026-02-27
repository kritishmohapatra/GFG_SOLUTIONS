class Solution:
    def findClosestPair(self,arr1, arr2, x):
        #code here
        i, j=0, m-1
        check=1e9+7
        ans=[]
        while i<n and j>=0:
            curr=arr1[i]+arr2[j]
            diff=abs(curr-x)
            if diff<check:
                check=diff
                ans=[arr1[i], arr2[j]]
            if curr==x:
                return [arr1[i], arr2[j]]
            elif curr>x:
                j-=1
            else:
                i+=1
        return ans