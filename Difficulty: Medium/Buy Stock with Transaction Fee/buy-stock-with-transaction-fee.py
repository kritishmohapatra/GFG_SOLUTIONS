class Solution:
    def maxProfit(self, arr, k):
        # Code here
        if not arr:
            return 0
        cash = 0
        hold = -arr[0]
        
        for i in range(1, len(arr)):
            prev_cash = cash
            
            cash = max(cash, hold + arr[i] - k)
            
            hold = max(hold, prev_cash - arr[i])
            
        return cash