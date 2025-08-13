class Solution:
    def minSoldiers(self, arr, k):
        # code here
        adjustments = [(k - (i % k)) % k for i in arr]
    
        # Step 2: Sort the adjustments
        adjustments.sort()
        
        # Step 3: Take the smallest half (ceiling of half the list length)
        half_len = (len(arr) + 1) // 2
        smallest_half = adjustments[:half_len]
        
        # Step 4: Return the sum of the smallest half
        return sum(smallest_half)