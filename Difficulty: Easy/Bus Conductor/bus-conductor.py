class Solution:
    def findMoves(self, c, p):
        # code here
        c.sort()
        p.sort()
        return sum([abs(c[i] - p[i]) for i in range(len(c))])
