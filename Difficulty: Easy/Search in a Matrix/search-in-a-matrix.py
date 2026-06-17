class Solution:
    def searchMatrix(self,matrix, x): 
    	# code here 
    	for i in range(len(matrix)):
    	    for j in range(len(matrix[0])):
    	        if matrix[i][j]==x:
    	            return 1
    	
