class Solution:
    def count(self, left, right, s):
        l=0
        while left>=0 and right<len(s):
            if s[left]==s[right]:
                l+=1
                left-=1
                right+=1
            else:
                break
        return l

    def countPS(self, s):
        # code here
        n=len(s)
        oc=0
        ec=0
        for i in range(n):
            oc+=self.count(i-1, i+1, s)
            
            ec+=self.count(i, i+1, s)
        return oc+ec
        