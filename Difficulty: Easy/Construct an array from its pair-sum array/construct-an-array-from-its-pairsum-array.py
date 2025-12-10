import math
class Solution:
    def constructArr(self, arr):
        # code here
        if len(arr) == 1:
            return [1, arr[0] - 1]

        # size of the original array 
        n = int((1 + math.isqrt(1 + 8 * len(arr))) / 2)
    
        # reconstruct the original array
        res = [0] * n
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2
        for i in range(1, n):
            res[i] = arr[i - 1] - res[0]
    
        return res