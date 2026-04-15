class Solution:
    def myAtoi(self, s):
        # code here
        sign=1
        res=0
        if len(s)==0:
            return 0
        i=0
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i]=="-" or s[i]=="+":
            if s[i]=="-":
                sign=-1
            i+=1
        while i<len(s) and "0"<=s[i]<="9":
            res=10*res+(ord(s[i])-ord("0"))
            if res>(2**31-1):
                return sign*(2**31-1) if sign==1 else -2**31
            i+=1
        return res*sign
        