class Solution:
    def minParentheses(self, s):
        # code here
        b=0
        unclo=0
        for c in s:
            if c=="(":
                b+=1
            elif c==")":
                b-=1
                if b<0:
                    unclo+=1
                    b=0
        return b+unclo
        