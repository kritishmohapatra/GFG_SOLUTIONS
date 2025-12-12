class Solution:
    def swapDiagonal(self, mat):
        
        s=len(mat)
        for i in range(s):
          mat[i][i], mat[i][s-i-1]= mat[i][s-i-1],mat[i][i]
       