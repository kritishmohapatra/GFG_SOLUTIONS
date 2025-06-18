class Solution:
    def caseSort(self,s):
        #code here
        low=[]
        up=[]
        li=0
        ui=0
        n=len(s)
        res=list(s)
        for i in s:
            if i.islower():
                low.append(i)
            else:
                up.append(i)
        low.sort()
        up.sort()
        for i in range(n):
            if s[i].islower():
                res[i]=low[li]
                li+=1
            else:
                res[i]=up[ui]
                ui+=1
        return "".join(res)