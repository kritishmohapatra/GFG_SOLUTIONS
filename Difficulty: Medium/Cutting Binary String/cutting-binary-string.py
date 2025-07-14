class Solution:
    def solve(self, i, s, powers, dp):
        # Base case
        if i == len(s):
            return 0
        # Memoization
        if dp[i] != -1:
            return dp[i]
        
        res = len(s) + 1
        num = 0
        for j in range(i, len(s)):
            num = num * 2 + int(s[j])  # binary to decimal
            if s[i] != '0' and num in powers:
                res = min(res, 1 + self.solve(j + 1, s, powers, dp))
        
        dp[i] = res
        return res

    def cuts(self, s):
        # code here
        if s[0] == '0':
            return -1
        
        dp = [-1] * len(s)
        powers = set()
        i = 1
        while i <= 1e9:
            powers.add(i)
            i *= 5
        
        ans = self.solve(0, s, powers, dp)
        return -1 if ans > len(s) else ans