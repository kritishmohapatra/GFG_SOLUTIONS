class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        ssum = ans = 0
        d = dict()
        
        
        for i in range(len(arr)):
            ssum += (1 if arr[i] > k else -1)
            if ssum > 0:
                ans = i + 1
            elif ssum - 1 in d:
                ans = max(ans, i - d[ssum - 1])
            
            d[ssum] = d.get(ssum, i)
            
        return ans