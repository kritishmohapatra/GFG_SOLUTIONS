from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        d=Counter(s)
        for k, v in d.items():
            if v==1:
                return k
        return "$"
    