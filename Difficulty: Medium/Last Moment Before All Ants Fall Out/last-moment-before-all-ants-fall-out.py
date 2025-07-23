class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        res=0
        for i in range(len(left)):
            res=max(res, left[i])
        for j in range(len(right)):
            res=max(res, n-right[j])
        return res