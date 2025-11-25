class Solution:
	def andInRange(self, l, r):
		# code here
		shiftCount = 0

    # Iterate through every bit of a and b
    # simultaneously if l == r then we know that beyond
        # that the AND value will remain constant
        while l != r and l > 0:
            shiftCount += 1
            l = l >> 1
            r = r >> 1
    
        return (l << shiftCount)
    		
