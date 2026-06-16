import math
class Solution:
    def getDivisors(self, n):
        # code here
        ans=[]
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                ans.append(i)
                if i!=n//i:
                    ans.append(n//i)
        ans.sort()
        return ans