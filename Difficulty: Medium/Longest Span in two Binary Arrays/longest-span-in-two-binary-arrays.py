class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        n=len(a1)
        res=0
        dif={}
        s1=0
        s2=0
        for i in range(n):
            s1+=a1[i]
            s2+=a2[i]
            cd=s1-s2
            if cd==0:
                res=max(res, i+1)
            elif cd in dif:
                res=max(res, i-dif[cd])
            else:
                dif[cd]=i 
        return res