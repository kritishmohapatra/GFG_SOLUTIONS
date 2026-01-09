class Solution:
    def count(self, s, k):
        n=len(s)
        ans=0
        freq=[0]*26
        dis=0
        i=0
        for j in range(n):
            freq[ord(s[j])-ord("a")]+=1
            if freq[ord(s[j])-ord("a")]==1:
                dis+=1
            while dis>k:
                freq[ord(s[i])-ord("a")]-=1
                if freq[ord(s[i])-ord("a")]==0:
                    dis-=1
                i+=1
            ans+=j-i+1
        return ans
    def countSubstr (self, s, k):
        # Code here
        n=len(s)
        ans=self.count(s, k)-self.count(s, k-1)
        return ans