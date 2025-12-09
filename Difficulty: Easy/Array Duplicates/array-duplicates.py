from collections import Counter

class Solution:
    def findDuplicates(self, arr):
        # code here
        k=[]
        a=dict(Counter(arr))
        for key, value in a.items():
            if value>1:
                k.append(key)
        if len(k)==0:
            return []
        else:
            k.sort()
            return k
        