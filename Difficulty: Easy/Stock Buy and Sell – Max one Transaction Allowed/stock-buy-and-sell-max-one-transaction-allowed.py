class Solution:
    def maxProfit(self, prices):
        # code here
        ans=0
        m=prices[0]
        for i in range(1, len(prices)):
            ans=max(ans, prices[i]-m)
            m=min(m, prices[i])
        return ans