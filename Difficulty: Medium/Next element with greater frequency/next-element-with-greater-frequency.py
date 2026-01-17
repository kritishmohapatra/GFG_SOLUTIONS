from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        # code here
        c=Counter(arr)
        n=len(arr)
        res=[-1]*n
        s=[]
        for i in range(n):
            while s and c[arr[i]]>c[arr[s[-1]]]:
                res[s.pop()]=arr[i]
            s.append(i)
        return res