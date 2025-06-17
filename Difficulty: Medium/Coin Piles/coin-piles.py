from bisect import bisect_right
import itertools
class Solution:
    def minimumCoins(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]
    
        ans = float('inf')
    
        for i in range(n):
            prev = prefix[i-1] if i > 0 else 0
    
            pos = bisect_right(arr, arr[i] + k)
    
            total = 0
            if pos < n:
                total = prefix[-1] - (prefix[pos-1] if pos > 0 else 0)
    
            allowed = (n - pos) * (arr[i] + k)
    
            extracoins = prev + total - allowed
    
            ans = min(ans, extracoins)
    
        return ans
        