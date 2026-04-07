class Solution:
    def segregate0and1(self, arr):
        # code here
        j=-1
        for i in range(0, len(arr)):
            if arr[i]==1:
                j=i
                break
        if j==-1:
            return arr
        for i in range(j+1, len(arr)):
            if arr[i]==0:
                (arr[j], arr[i])=(arr[i], arr[j])
                j+=1
        return arr