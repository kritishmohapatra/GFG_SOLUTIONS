class Solution:
    def sumDiffPairs(self, arr, K):
        # code here
        N=len(arr)
        
        arr.sort()
        
        res = 0
        
        
        while N-2 >= 0:
            
            if arr[N-1] - arr[N-2] < K:
                
                res += (arr[N-1] + arr[N-2])
                
                N -=2
                
            else:
                
                N -=1
                
        return res