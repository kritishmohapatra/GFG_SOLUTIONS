class Solution:
    def printDivisors(self, n):
        #code here
        k=[]
        for i in range(1,int(math.sqrt(n)) + 1 ):
            if n%i==0:
                k.append(i)
                if i!=n//i:
                    k.append(n//i)
        k.sort()
            
        return k
