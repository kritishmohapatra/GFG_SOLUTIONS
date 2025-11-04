#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        st=[]
        for c in postfix:
            if c.isalnum():
                st.append(c)
            else:
                op2=st.pop()
                op1=st.pop()
                st.append(f"({op1}{c}{op2})")
        return st[-1]