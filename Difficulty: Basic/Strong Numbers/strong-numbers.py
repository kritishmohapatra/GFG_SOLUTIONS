class Solution:
    def isStrong(self, n):
        # code here
        fact = [
        1, 1, 2, 6, 24,
        120, 720, 5040, 40320, 362880
        ]
        o=n
        s=0
        while n>0:
            r=n%10
            s+=fact[r]
            n//=10
        return o==s
