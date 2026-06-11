class Solution:
    def findIndex(self, s):
        # code here 
        n=len(s)
        o=0
        c=0
        for i in range(n):
            if s[i]==")":
                c+=1
        for i in range(n+1):
            if o==c:
                return i
            if i<n:
                if s[i]=="(":
                    o+=1
                if s[i]==")":
                    c-=1
        return -1
            
