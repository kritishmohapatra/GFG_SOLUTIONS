class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        m1={}
        se2=set()
        for c1, c2 in zip(s1, s2):
            if c1 in m1:
                if m1[c1]!=c2:
                    return False
            else:
                if c2 in se2:
                    return False
            m1[c1]=c2
            se2.add(c2)
        return True