class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        n=len(mices)
        ans=0
        for i in range(n):
            if ans<(abs(mices[i]-holes[i])):
                ans=abs(mices[i]-holes[i])
        return ans
        