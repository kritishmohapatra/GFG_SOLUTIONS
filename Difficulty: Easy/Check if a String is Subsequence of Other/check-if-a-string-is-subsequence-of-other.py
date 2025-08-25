class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        n=len(s1)
        m=len(s2)
        i, j=0, 0
        while (i<n and j<m):
            if s1[i]==s2[j]:
                i+=1
            j+=1
        return i==n