class Solution:
	def isWordExist(self, mat, word):
		# Code here
		m=len(mat)
        n=len(mat[0])
        direc=[(1, 0),(-1, 0), (0, 1), (0, -1)]
        def find(mat, i, j, idx, word):
            if idx==len(word):
                return True
            if i<0 or j<0 or j>=n or i>=m or mat[i][j]=="$":
                return False
            if mat[i][j]!=word[idx]:
                return False
            t=mat[i][j]
            mat[i][j]="$"
            for d in direc:
                new_i=i+d[0]
                new_j=j+d[1]
                if find(mat,new_i, new_j, idx+1, word):
                    return True
            mat[i][j]=t
            return False
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==word[0] and find(mat, i, j, 0, word):
                    return True
                    
        return False