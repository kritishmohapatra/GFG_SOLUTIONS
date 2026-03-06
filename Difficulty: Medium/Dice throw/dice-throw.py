class Solution:
    def solve(self, m, n, x, s, dp):
        if n == 0 and s == x:
            return 1
        if n == 0 or s > x:
            return 0
        if dp[n][s] != -1:
            return dp[n][s]
        
        cnt = 0
        for i in range(1, m + 1):
            cnt += self.solve(m, n - 1, x, s + i, dp)
        
        dp[n][s] = cnt
        return cnt 

    def noOfWays(self, m, n, x):
        dp = [[-1 for _ in range(x + 1)] for _ in range(n + 1)]
        return self.solve(m, n, x, 0, dp)