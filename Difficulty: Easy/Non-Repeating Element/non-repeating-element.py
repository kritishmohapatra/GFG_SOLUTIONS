from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        # code here
        c=Counter(arr)
        for i in arr:
            if c[i]==1:
                return i
        return 0
