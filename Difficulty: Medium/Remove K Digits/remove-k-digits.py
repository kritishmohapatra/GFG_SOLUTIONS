class Solution:
    def removeKdig(self, s, k):
        # code here
        st=[]
        for d in s:
            while st and k>0 and st[-1]>d:
                st.pop()
                k-=1
            st.append(d)
        while st and k>0:
            st.pop()
            k-=1
        if not st:
            return "0"
        res=""
        while st:
            res+=st.pop()
        res=res.rstrip("0")
        res=res[::-1]
        if not res:
            return "0"
        return res