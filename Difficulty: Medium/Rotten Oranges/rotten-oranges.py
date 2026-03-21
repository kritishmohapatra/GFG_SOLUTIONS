from collections import deque
class Solution:
	def orangesRot(self, mat):
		# code here
		n=len(mat)
        m=len(mat[0])
        q=deque()
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==2:
                    q.append([i, j, 0])
                    vis[i][j]=2
                else:
                    vis[i][j]=0
        t=0
        dr=[-1, 0,1, 0]
        dc=[0,1,0,-1]
        while q:
            r, c, tm=q.popleft()
            t=max(tm ,t)
            for i in range(4):
                nrow=dr[i]+r
                ncol=dc[i]+c 
                if 0<=nrow<n and 0<=ncol<m and mat[nrow][ncol]==1 and vis[nrow][ncol]!=2:
                    q.append([nrow, ncol, t+1])
                    vis[nrow][ncol]=2 
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and vis[i][j]!=2:
                    return -1 
        return t