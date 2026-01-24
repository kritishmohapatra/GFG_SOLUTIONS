class Solution:
    def findWays(self, n):
        # code here
        if n % 2 != 0:
            return 0
        
        pairs = n // 2
        catalan = 1
        
        # Iterative formula for Catalan Number: 
        # C(n) = (1 / (n + 1)) * (2n choose n)
        # Using the recurrence: C(i) = C(i-1) * (4i - 2) / (i + 1)
        for i in range(1, pairs + 1):
            catalan = catalan * 2 * (2 * i - 1) // (i + 1)
            
        return int(catalan)