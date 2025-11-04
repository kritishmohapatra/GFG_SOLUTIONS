#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        st=[]
        for c in reversed(pre_exp):
            if c.isalnum():
                st.append(c)
            else:
                op2=st.pop()
                op1=st.pop()
                st.append(op2+op1+c)
        return st[0]