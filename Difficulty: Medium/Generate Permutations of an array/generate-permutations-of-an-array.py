class Solution:
    def permuteDist(self, arr):
        # code here
        res=[]
        def swap(arr, i, j):
            if i!=j:
                arr[i], arr[j]= arr[j], arr[i]
        def rec(arr, s):
            if s==len(arr):
                res.append(list(arr))
            for i in range(s, len(arr)):
                swap(arr, i, s)
                rec(arr, s+1)
                swap(arr, i, s)
        rec(arr, 0)
        return res
        
        