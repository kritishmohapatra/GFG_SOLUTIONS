import math
class Solution:
    def isPrime(self, n):
        # code here
        if n==1:
            return 0
        a=int(math.sqrt(n))
        for i in range(2,a+1):
           if(n %i==0):
                return 0
        return 1