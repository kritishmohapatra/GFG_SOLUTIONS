class Solution:
    def searchMatrix(self, mat, x):
        # code here
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==x:
                    return True
        return False