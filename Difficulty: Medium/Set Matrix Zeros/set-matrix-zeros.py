#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        col0 = 1
        n=len(mat)
        m=len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
    
                    if j != 0:
                        mat[0][j] = 0
                    else:
                        col0 = 0
    
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] != 0:
                    if mat[i][0] == 0 or mat[0][j] == 0:
                        mat[i][j] = 0
    
        if mat[0][0] == 0:
            for j in range(m):
                mat[0][j] = 0
        if col0 == 0:
            for i in range(n):
                mat[i][0] = 0
    
        return mat
            


