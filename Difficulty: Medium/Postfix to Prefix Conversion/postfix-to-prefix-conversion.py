#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        st=[]
        for c in post_exp:
            if c.isalnum():
                st.append(c)
            else:
                op2=st.pop()
                op1=st.pop()
                st.append(c+op1+op2)
        return st[-1]