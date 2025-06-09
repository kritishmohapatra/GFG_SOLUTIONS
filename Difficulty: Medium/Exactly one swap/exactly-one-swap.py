class Solution:
    def countStrings(self, s): 
        #code here
        n=len(s)
        ans=0
        mp=[0]*26
        for i in range(n):
            ans+=i-mp[(ord(s[i]))-ord("a")]
            mp[(ord(s[i]))-ord("a")]+=1
        for i in range(26):
            if mp[i]>1:
                ans+=1
                break 
        return ans
            