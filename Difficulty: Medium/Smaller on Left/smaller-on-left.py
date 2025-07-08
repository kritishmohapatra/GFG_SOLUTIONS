
class Solution:
    def leftSmaller(self, arr):
        res=[]
        st=[]
        for num in arr:
            while st and st[-1]>=num:
                st.pop()
            if not st:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(num)
        return res
                 