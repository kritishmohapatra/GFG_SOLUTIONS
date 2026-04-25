class Solution:
    def commonElements(self, A, B, C):
        # code here
        k=list(set(A) & set(B) & set(C))
        k.sort()
        return k