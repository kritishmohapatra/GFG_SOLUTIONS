class Solution:
    def solve(self, i, j, n, mat, dp):
        # Base case
        if i < 0 or j < 0 or i > 3 or j > 2 or mat[i][j] == -1:
            return 0
        if n == 0:
            return 1
        if dp[i][j][n] != -1:
            return dp[i][j][n]

        # Recursive case: stay or move in 4 directions
        ans = (self.solve(i, j, n - 1, mat, dp) +
               self.solve(i + 1, j, n - 1, mat, dp) +
               self.solve(i - 1, j, n - 1, mat, dp) +
               self.solve(i, j + 1, n - 1, mat, dp) +
               self.solve(i, j - 1, n - 1, mat, dp))
        dp[i][j][n] = ans
        return ans
	def getCount(self, n):
		# code here
		mat = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [-1, 1, -1]
        ]

        dp = [[[-1 for _ in range(n)] for _ in range(3)] for _ in range(4)]
        count = 0

        for i in range(4):
            for j in range(3):
                if mat[i][j] != -1:
                    count += self.solve(i, j, n - 1, mat, dp)
        return count