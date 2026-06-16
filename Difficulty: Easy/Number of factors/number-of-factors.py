import math
class Solution:
    def countFactors (self, n):
        # code here
        c=0
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                c+=1
                if n//i!=i:
                    c+=1
        return c
        