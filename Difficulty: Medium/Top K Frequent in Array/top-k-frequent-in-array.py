from collections import Counter
class Solution:
	def topKFreq(self, arr, k):
		# Code here
		
		c=Counter(arr)
        f=dict(c)
        ans=sorted(f.keys(), key=lambda x:(-f[x], -x))
        return ans[:k]
        