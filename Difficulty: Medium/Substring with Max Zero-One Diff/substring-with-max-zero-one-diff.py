class Solution:
	def maxSubstring(self, s):
		# code here
		d=0
		mxd=(1 if s[0]=="0" else -1)
		for i in s:
		    d+=(1 if i=="0" else -1)
		    mxd=max(mxd, d)
		    if d<0:
		        d=0
		return mxd
		