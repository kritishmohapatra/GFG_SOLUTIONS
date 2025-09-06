class Solution:
    def prec(self, c):
        if c=="^":
            return 3
        elif c=="/" or c=="*":
            return 2
        elif c=="+" or c=="-":
            return 1
        else:
            return -1
            
        
    def infixtoPostfix(self, s):
        #code here
        st=[]
        res=""
        for c in s:
            if c.isalnum():
                res+=c
            elif c=="(":
                st.append(c)
            elif c==")":
                while st and st[-1]!="(":
                    res+=st.pop()
                st.pop()
            else:
                while st and self.prec(c)<=self.prec(st[-1]):
                    res+=st.pop()
                st.append(c)
                
        while st:
            res+=st.pop()
        return res