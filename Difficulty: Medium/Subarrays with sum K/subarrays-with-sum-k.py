from collections import defaultdict
class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        m=defaultdict(int)
        p=0
        cnt=0
        m[0]=1
        for i in range(len(arr)):
            p+=arr[i]
            r=p-k
            cnt+=m[r]
            m[p]+=1
        return cnt
        