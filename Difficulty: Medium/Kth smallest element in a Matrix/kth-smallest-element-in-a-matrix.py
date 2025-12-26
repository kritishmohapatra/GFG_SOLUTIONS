class Solution:
    def kthSmallest(self, mat, k):
        # code here
        arr = [j for i in mat for j in i]
        arr.sort()
        return arr[k-1]