class Solution:
    def generateBinary(self, n):
        # code here
        k=[]
        for i in range(1, n+1):
            p=bin(i).replace("0b","")
            k.append(p)
        return k