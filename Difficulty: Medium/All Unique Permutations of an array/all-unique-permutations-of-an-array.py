from itertools import permutations

class Solution:
    def uniquePerms(self, arr):
        # code here 
        res=list(sorted(set(permutations(arr))))
        return res