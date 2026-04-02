class Solution:
    def diagView(self, mat):
        n = len(mat)
        output = []
        for i in range(n):
            for x in range(i + 1):
                output.append(mat[x][i - x])
        for i in range(1, n):
            for x in range(i, n):
                output.append(mat[x][n - 1 + i - x])
        return output