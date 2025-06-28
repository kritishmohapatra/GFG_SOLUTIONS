class Solution:
    def countLessEq(self, a, b):
        # code here
        n = len(a)
        m = len(b)
    
        # to store the result
        res = [0] * n
        maxi = max(b)
        # to store frequency of elements in b[]
        cnt = [0] * (maxi + 1)
        
        for i in range(m):
            cnt[b[i]] += 1
    
        # transform cnt[] to prefix sum array
        for i in range(1, (maxi + 1)):
            cnt[i] += cnt[i - 1]
    
        # loop for each element of a[]
        for i in range(n):
            res[i] = cnt[min(a[i], maxi)]
    
        return res
            
        