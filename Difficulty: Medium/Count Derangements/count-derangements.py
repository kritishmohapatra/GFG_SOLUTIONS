class Solution:
    def derangeCount(self, n: int) -> int:
        # code here
        if n == 1:
            return 0
        if n == 2:
            return 1
    
        # Variables to store previous two results
        # Equivalent to dp[1]
        prev2 = 0
    
        # Equivalent to dp[2]
        prev1 = 1
    
        # Calculate derangements using the 
        # optimized space approach
        for i in range(3, n + 1):
            curr = (i - 1) * (prev1 + prev2)
            prev2 = prev1
            prev1 = curr
    
        return prev1