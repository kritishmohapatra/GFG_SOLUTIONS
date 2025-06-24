class Solution:
    def maxSubseq(self, s, k):
        #code here
        n=len(s)
        res=""
        rem=k
        for i in range(n):
            while res and rem>0 and res[-1]<s[i]:
                res=res[:-1]
                rem-=1
            res+=s[i]
        return res[:n-k]
        
