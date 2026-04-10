class Solution:
    def countIncreasing(self, arr):
        # code here.
        ans = 0
        start = -1
        
        for i in range(len(arr)):
            if start == -1 or arr[i - 1] >= arr[i]:
                start = i

            ans += (i - start)
        
        return ans
