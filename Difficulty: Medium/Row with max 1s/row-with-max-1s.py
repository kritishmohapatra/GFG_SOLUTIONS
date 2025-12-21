class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxones=0
        ans=-1
        for i in range(len(arr)):
            count=0
            for j in range(len(arr[0])):
                if arr[i][j]==1:
                    count+=1
            if count>maxones:
                maxones=count
                ans=i
        return ans