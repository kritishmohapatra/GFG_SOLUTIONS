class Solution:
	def getLPSLength(self, s):
		# code here
		lp=[0]*(len(s))
        pre=0
        suf=1
        while suf<len(s):
            if s[pre]==s[suf]:
                lp[suf]=pre+1
                pre+=1
                suf+=1
            else:
                if pre==0:
                    lp[suf]=0
                    suf+=1
                else:
                    pre=lp[pre-1]
        return  lp[-1]
		