from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        # code here
        m=defaultdict(int)
        m[0]=1
        xor=0
        ans=0
        for i in range(len(arr)):
            xor=xor^arr[i]
            x=xor^k
            ans+=m[x]
            m[xor]+=1
        return ans
